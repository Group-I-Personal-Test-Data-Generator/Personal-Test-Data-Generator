from __future__ import annotations
import re
from typing import List, Tuple

from backend.FakeInfoService.repositories.settings import Settings, get_conn

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS postal_code (
    postal_code TEXT NOT NULL,
    town_name   TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_postal_code ON postal_code(postal_code);
"""

INSERT_TUPLE_RE = re.compile(r"\(([^()]+)\)")
STRING_RE = re.compile(r"^\s*'([^']*)'\s*$|^\s*\"([^\"]*)\"\s*$|^\s*([^,]+)\s*$")


def ensure_db_loaded(settings: Settings) -> None:
    with get_conn(settings) as conn:
        conn.executescript(SCHEMA_SQL)
        count = conn.execute("SELECT COUNT(*) AS c FROM postal_code").fetchone()[0]
        if count > 0:
            return

    # Try to import from SQL file if present
    towns: List[Tuple[str, str]] = []
    try:
        with open(settings.addresses_sql_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip()
                if not s or not s.upper().startswith("INSERT"):
                    continue

                # Parse only tuples after the VALUES keyword (skip the column list)
                up = s.upper()
                idx = up.find("VALUES")
                if idx == -1:
                    continue
                values_part = s[idx + len("VALUES"):]

                # Extract the tuples from the VALUES part
                for tup in INSERT_TUPLE_RE.findall(values_part):
                    parts = []
                    current = []
                    in_quote = None
                    for ch in tup:
                        if ch in ('"', "'"):
                            if in_quote is None:
                                in_quote = ch
                            elif in_quote == ch:
                                in_quote = None
                            current.append(ch)
                        elif ch == ',' and in_quote is None:
                            parts.append(''.join(current).strip())
                            current = []
                        else:
                            current.append(ch)
                    if current:
                        parts.append(''.join(current).strip())

                    if len(parts) < 2:
                        continue
                    pc = _parse_literal(parts[0])
                    town = _parse_literal(parts[1])

                    # Skip header-like placeholders (e.g. `cPostalCode`)
                    if not pc or not town:
                        continue
                    if pc.startswith("`") or town.startswith("`"):
                        continue

                    towns.append((pc, town))
    except FileNotFoundError:
        towns = []

    # Fallback seed data if nothing was imported
    if not towns:
        towns = [
            ("1000", "København K"),
            ("2000", "Frederiksberg"),
            ("2100", "København Ø"),
            ("8000", "Aarhus C"),
            ("5000", "Odense C"),
            ("9000", "Aalborg"),
        ]

    with get_conn(settings) as conn:
        conn.executemany("INSERT INTO postal_code (postal_code, town_name) VALUES (?, ?)", towns)
        conn.commit()


def _parse_literal(s: str):
    m = STRING_RE.match(s)
    if not m:
        return None
    val = next((g for g in m.groups() if g is not None), None)
    if val is None:
        return None
    return val.replace("\\'", "'").replace('\\"', '"')

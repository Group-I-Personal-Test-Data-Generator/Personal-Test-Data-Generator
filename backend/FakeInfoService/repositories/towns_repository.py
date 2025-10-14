from __future__ import annotations
import random
import sqlite3
from typing import Tuple

from repositories.settings import Settings, get_conn


def pick_random_town(conn: sqlite3.Connection) -> Tuple[str, str]:
    cur = conn.execute("SELECT COUNT(*) AS c FROM postal_code")
    total = cur.fetchone()[0]
    if total <= 0:
        return ("0000", "Ukendt")
    offset = random.randint(0, total - 1)
    row = conn.execute(
        "SELECT postal_code, town_name FROM postal_code LIMIT 1 OFFSET ?",
        (offset,),
    ).fetchone()
    if not row:
        return ("0000", "Ukendt")
    return (str(row["postal_code"]), str(row["town_name"]))
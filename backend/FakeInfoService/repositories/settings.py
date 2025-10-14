from __future__ import annotations
import os
import random
import sqlite3
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Settings:
    port: int
    sqlite_db_path: str
    addresses_sql_path: str
    names_json_path: str
    rng_seed: str | None

    @staticmethod
    def from_env() -> "Settings":
        port = int(os.getenv("PORT", "5002"))
        base = Path.cwd()
        sqlite_db_path = os.getenv("SQLITE_DB_PATH", str(base / "addresses.sqlite3"))
        addresses_sql_path = os.getenv("ADDRESSES_SQL_PATH", str(base / "data" / "addresses.sql"))
        names_json_path = os.getenv("NAMES_JSON_PATH", str(base / "data" / "person-names.json"))
        rng_seed = os.getenv("RNG_SEED")
        if rng_seed is not None:
            try:
                random.seed(int(rng_seed))
            except ValueError:
                random.seed(rng_seed)
        return Settings(port, sqlite_db_path, addresses_sql_path, names_json_path, rng_seed)


def get_conn(settings: Settings) -> sqlite3.Connection:
    conn = sqlite3.connect(settings.sqlite_db_path)
    conn.row_factory = sqlite3.Row
    return conn
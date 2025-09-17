"""Create an SQLite database from the SQL schema file.

Creates clinic_simple.db in the repository root and applies sql/schema.sql.
"""
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "clinic_simple.db"
SCHEMA_PATH = ROOT / "sql" / "schema.sql"


def create_db():
    if not SCHEMA_PATH.exists():
        raise SystemExit(f"Schema file not found: {SCHEMA_PATH}")

    with sqlite3.connect(DB_PATH) as conn:
        sql = SCHEMA_PATH.read_text()
        conn.executescript(sql)
    print(f"Created database: {DB_PATH}")


if __name__ == "__main__":
    create_db()

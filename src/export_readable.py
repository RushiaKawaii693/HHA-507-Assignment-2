"""Export clinic_simple.db into a SQL dump and a CSV of the patients table.

Creates an outputs/ directory with:
- clinic_simple_dump.sql  (full sqlite text dump)
- patients_export.csv     (CSV of patients table)
"""
from pathlib import Path
import sqlite3
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "clinic_simple.db"
OUT_DIR = ROOT / "outputs"


def export_db():
    if not DB_PATH.exists():
        raise SystemExit(f"Database not found: {DB_PATH}")

    OUT_DIR.mkdir(exist_ok=True)

    # SQL dump using iterdump
    dump_path = OUT_DIR / "clinic_simple_dump.sql"
    with sqlite3.connect(DB_PATH) as conn, open(dump_path, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")

    # Export patients table to CSV using pandas for convenience
    csv_path = OUT_DIR / "patients_export.csv"
    df = pd.read_sql_query("SELECT * FROM patients", f"sqlite:///{DB_PATH}")
    df.to_csv(csv_path, index=False)

    print(f"Wrote SQL dump: {dump_path}")
    print(f"Wrote patients CSV: {csv_path}")


if __name__ == "__main__":
    export_db()

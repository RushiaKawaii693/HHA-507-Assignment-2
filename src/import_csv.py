"""Load data/patients.csv into the patients table using pandas + SQLAlchemy.

This script expects clinic_simple.db to already exist (created by create_db.py).
It appends rows from the CSV into the patients table.
"""
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "clinic_simple.db"
CSV_PATH = ROOT / "data" / "patients.csv"


def import_csv():
    if not DB_PATH.exists():
        raise SystemExit(f"Database not found: {DB_PATH}. Run create_db.py first.")
    if not CSV_PATH.exists():
        raise SystemExit(f"CSV not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    engine = create_engine(f"sqlite:///{DB_PATH}")
    # Strategy: write CSV to a temporary table, then upsert into patients
    with engine.begin() as conn:
        # create temp table
        conn.execute(text("DROP TABLE IF EXISTS _tmp_patients"))
        df.to_sql("_tmp_patients", conn, if_exists="replace", index=False)

        # Insert or replace into patients using patient_id as primary key
        # This will replace rows with the same patient_id and insert new ones
        conn.execute(text(
            "INSERT OR REPLACE INTO patients(patient_id, birth_date, primary_icd10, last_cpt, last_visit_dt) "
            "SELECT patient_id, birth_date, primary_icd10, last_cpt, last_visit_dt FROM _tmp_patients"
        ))

        # drop temp table
        conn.execute(text("DROP TABLE IF EXISTS _tmp_patients"))

    print(f"Imported {len(df)} rows into patients table (upsert)")


if __name__ == "__main__":
    import_csv()

"""Run each query in sql/analysis.sql and print results to the console.

This is a small verification helper so you can see the analysis query outputs
without opening DB Browser.
"""
from pathlib import Path
import sqlite3


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "clinic_simple.db"
ANALYSIS_SQL = ROOT / "sql" / "analysis.sql"


def run_analysis():
    if not DB_PATH.exists():
        raise SystemExit(f"Database not found: {DB_PATH}. Create it first.")
    if not ANALYSIS_SQL.exists():
        raise SystemExit(f"analysis.sql not found: {ANALYSIS_SQL}")

    sql_text = ANALYSIS_SQL.read_text()
    # split queries by semicolon for simple cases
    queries = [q.strip() for q in sql_text.split(';') if q.strip()]

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for i, q in enumerate(queries, start=1):
            print(f"\n-- Query {i} --")
            try:
                cur.execute(q)
            except Exception as e:
                print(f"Error executing query: {e}\nQuery:\n{q}")
                continue
            rows = cur.fetchmany(10)
            # print column names
            col_names = [d[0] for d in cur.description] if cur.description else []
            if col_names:
                print('\t'.join(col_names))
            for r in rows:
                print('\t'.join(str(x) for x in r))
            # show count of remaining rows if any
            more = cur.fetchmany(1)
            if more:
                print("... (more rows) ...")


if __name__ == "__main__":
    run_analysis()

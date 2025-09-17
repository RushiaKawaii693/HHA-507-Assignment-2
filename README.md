# Single-table patient roster (SQLite + Pandas)

Quick run (PowerShell)

1) Create and activate a virtual environment (optional but recommended):

   python -m venv .venv
   .\\.venv\\Scripts\\Activate.ps1

2) Install dependencies:

   pip install -r requirements.txt

3) Create the SQLite database from the schema:

   python src/create_db.py

4) Import the CSV into the database:

   python src/import_csv.py

5) (Optional) Run the bundled analysis queries and print results:

   python src/verify_analysis.py

Open `clinic_simple.db` in DB Browser for SQLite and run `sql/analysis.sql` if you prefer a GUI.

Deliverables checklist

- `sql/schema.sql` — single-table schema
- `data/patients.csv` — >=25 rows
- `src/create_db.py` and `src/import_csv.py`
- `sql/analysis.sql` — analysis queries
- `clinic_simple.db` — generated database
# Single-table patient roster (SQLite + Pandas)

Run steps:

1. Install dependencies:

   pip install -r requirements.txt

2. Create the database from the schema:

   python src/create_db.py

3. Load the CSV into the database:

   python src/import_csv.py

Open `clinic_simple.db` in DB Browser for SQLite and run `sql/analysis.sql`.
# New-folder
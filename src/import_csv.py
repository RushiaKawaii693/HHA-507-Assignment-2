import pandas as pd
from sqlalchemy import create_engine

def import_csv():
    engine = create_engine("sqlite:///clinic_simple.db")
    df = pd.read_csv("data/patients.csv")
    df.to_sql("patients", con=engine, if_exists="append", index=False)
    print(f"Imported {len(df)} rows into patients table.")

if __name__ == "__main__":
    import_csv()

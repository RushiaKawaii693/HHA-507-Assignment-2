import sqlite3

def create_database():
    conn = sqlite3.connect("clinic_simple.db")
    cur = conn.cursor()

    with open("sql/schema.sql", "r") as f:
        schema = f.read()
    cur.executescript(schema)

    conn.commit()
    conn.close()
    print("Database created successfully (clinic_simple.db).")

if __name__ == "__main__":
    create_database()


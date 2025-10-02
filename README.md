# Health SQLite Lite

# Project Overview
Health SQLite Lite is a simple project that demonstrates how to manage and analyze healthcare data using SQLite and pandas in Python. The project provides scripts to create a sample clinic database, import patient data from CSV, and perform SQL-based data analysis for easy exploration and reporting.



## How to run
1. Install dependencies: `pip install -r requirements.txt`
2. Create database: `python src/create_db.py`
3. Import patients CSV: `python src/import_csv.py`
4. Open `clinic_simple.db` in DB Browser for SQLite and run `sql/analysis.sql`

# Query results section:
A) Row count
Description: Counts the total number of patients in the dataset.

Result: 
<img width="1919" height="1079" alt="Screenshot 2025-10-01 195915" src="https://github.com/user-attachments/assets/240f1bd3-72b7-412c-af87-a7a1ff625881" />

Explanation: The database contains 25 patients.

B) Top primary diagnoses by count
Description: Lists ICD-10 primary diagnoses and how many patients have each, ranked by frequency.

Result:
<img width="1919" height="1079" alt="Screenshot 2025-10-01 200640" src="https://github.com/user-attachments/assets/ef8f3cce-86b5-4bfa-84c0-d22e04b54655" />

Explanation: The most common diagnosis is E11.9 (Type 2 diabetes mellitus without complications) and K21.9 (Gastro-esophageal reflux disease without esophagitis) appearing in 3 patients each.

C) Office-visit CPTs since Jan 1, 2025
Description: Retrieves patients with office-visit CPT codes (992xx series) and visits on or after 2025-01-01.

Result:
<img width="1919" height="1079" alt="Screenshot 2025-10-01 195940" src="https://github.com/user-attachments/assets/62907aff-ace1-4c96-b66c-f478c8352176" />

Explanation: The results show recent patient visits coded as office visits, sorted so the most recent ones appear first.

D) 5 oldest patients by age
Description: Finds the five oldest patients based on birthdate and calculates their age.

Result:
<img width="1917" height="1078" alt="Screenshot 2025-10-01 195958" src="https://github.com/user-attachments/assets/88ef232e-0996-416f-8cbf-89ec47ef044b" />

Explanation: The oldest patient in the dataset is 76 years old, and the results list the top five by age.

<img width="1919" height="1079" alt="Screenshot 2025-10-01 195915" src="https://github.com/user-attachments/assets/240f1bd3-72b7-412c-af87-a7a1ff625881" />



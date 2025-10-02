-- A) Row count
SELECT COUNT(*) AS n_patients FROM patients;

-- B) Top primary diagnoses by count
SELECT primary_icd10, COUNT(*) AS n
FROM patients
GROUP BY primary_icd10
ORDER BY n DESC;

-- C) Office-visit CPTs since Jan 1, 2025
SELECT patient_id, last_cpt, last_visit_dt
FROM patients
WHERE last_cpt LIKE '992%' AND last_visit_dt >= '2025-01-01'
ORDER BY last_visit_dt DESC;

-- D) 5 oldest patients by age
SELECT
  patient_id,
  birth_date,
  last_visit_dt,
  CAST((julianday(date('now')) - julianday(birth_date)) / 365.25 AS INT) AS age_years
FROM patients
ORDER BY age_years DESC
LIMIT 5;

-- E) Data quality check
SELECT *
FROM patients
WHERE primary_icd10 = '' OR last_cpt = '';

-- Example: patients with missing codes or placeholder values
SELECT *
FROM patients
WHERE primary_icd10 IS NULL 
   OR primary_icd10 = 'UNK'
   OR last_cpt IS NULL
   OR last_cpt = '00000';


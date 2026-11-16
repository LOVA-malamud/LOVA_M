DROP TABLE IF EXISTS medical_files;
DROP TABLE IF EXISTS patients;
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    blood_type TEXT
);

CREATE TABLE medical_files (
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_ref INTEGER UNIQUE,
    allergies TEXT,
    emergency_contact TEXT,
    FOREIGN KEY (patient_ref) REFERENCES patients(patient_id)
);


INSERT INTO patients (patient_name, blood_type) VALUES ('Dr. Aisha Khan', 'O+');
INSERT INTO patients (patient_name, blood_type) VALUES ('Marcus Williams', 'AB-');
INSERT INTO patients (patient_name, blood_type) VALUES ('Dr. Priya Singh', 'B+');

INSERT INTO medical_files (patient_ref, allergies, emergency_contact) 
VALUES (1, 'Penicillin', '+1-555-0101');

INSERT INTO medical_files (patient_ref, allergies, emergency_contact) 
VALUES (2, 'None', '+1-555-0202');


SELECT 
    p.patient_id,
    p.patient_name,
    p.blood_type,
    m.allergies,
    m.emergency_contact
FROM patients p
LEFT JOIN medical_files m ON p.patient_id = m.patient_ref;


INSERT INTO medical_files (patient_ref, allergies, emergency_contact) 
VALUES (1, 'Peanuts', '+1-555-9999');


DELETE FROM patients WHERE patient_id = 1;
SELECT * FROM medical_files;

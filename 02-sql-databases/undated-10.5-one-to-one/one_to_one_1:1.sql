DROP TABLE IF EXISTS id_cards;
DROP TABLE IF EXISTS citizens;  

CREATE TABLE citizens (
    citizen_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    city TEXT
);

CREATE TABLE id_cards (
    citizen_id INTEGER PRIMARY KEY,
    card_number TEXT UNIQUE NOT NULL,
    expires TEXT,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id) ON DELETE CASCADE
);

INSERT INTO citizens (full_name, city) VALUES ('Sophia Martinez', 'Barcelona');
INSERT INTO citizens (full_name, city) VALUES ('James Chen', 'Toronto');
INSERT INTO citizens (full_name, city) VALUES ('Amira Hassan', 'Cairo');


INSERT INTO id_cards (citizen_id, card_number, expires) VALUES (1, 'ID-2024-5521', '2032-12-15');
INSERT INTO id_cards (citizen_id, card_number, expires) VALUES (2, 'ID-2023-7744', '2031-08-22');


SELECT c.full_name, i.card_number
FROM citizens c
INNER JOIN id_cards i ON c.citizen_id = i.citizen_id;


SELECT c.full_name, COALESCE(i.card_number, 'No card') AS card_info
FROM citizens c
LEFT JOIN id_cards i ON c.citizen_id = i.citizen_id;

INSERT INTO id_cards (citizen_id, card_number, expires) VALUES (1, 'ID-9999-9999', '2040-01-01');

DELETE FROM citizens WHERE citizen_id = 1;

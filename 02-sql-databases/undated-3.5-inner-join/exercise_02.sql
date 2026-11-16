DROP TABLE IF EXISTS drivers;
DROP TABLE IF EXISTS cars;
CREATE TABLE drivers (
  id     INTEGER PRIMARY KEY,
  name   TEXT    NOT NULL,
  car_id INTEGER,
  FOREIGN KEY (car_id) REFERENCES cars(id)
);

INSERT INTO drivers VALUES
  (1,'Dana',1),
  (2,'Omar',2),
  (3,'Noa',NULL),
  (4,'Liam',3),
  (5,'Rina',NULL);

CREATE TABLE cars (
  id    INTEGER PRIMARY KEY,
  model TEXT    NOT NULL,
  price REAL    NOT NULL
);

INSERT INTO cars VALUES
  (1,'Toyota Corolla',22000),
  (2,'Honda Civic',24000),
  (3,'Ford Focus',19000),
  (4,'Tesla Model 3',42000);

SELECT d.name, c.model
FROM drivers d
LEFT JOIN cars c ON d.car_id = c.id;

SELECT d.name, c.model
FROM drivers d
LEFT JOIN cars c ON d.car_id = c.id
WHERE c.id IS NULL;

SELECT c.model
FROM cars c
LEFT JOIN drivers d ON d.car_id = c.id
WHERE d.id IS NULL;

SELECT d.dept_name, COUNT(e.id) AS employees_count
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id
GROUP BY d.dept_name;

SELECT e.name, COALESCE(d.budget, 0) AS budget
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;



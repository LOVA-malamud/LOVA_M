DROP TABLE IF EXISTS exam_results;
CREATE TABLE exam_results (
    id INT primary key,
    email TEXT NOT NULL UNIQUE,
    student_name TEXT not null,
    grade INT check (grade >= 0 and grade <= 100),
    status TEXT DEFAULT 'pending'

);
INSERT INTO exam_results (id, email, student_name, grade, status)
VALUES 
(1, 'dana@mail.com', 'Dana', 92, 'approved'),
(2, 'omar@mail.com', 'Omer', 76, 'pending'),
(3, 'noa@mail.com', 'Noa', 85, 'approved');

SELECT * FROM exam_results WHERE status = 'approved';

SELECT * FROM exam_results WHERE student_name like 'd%' and email like 'd%';
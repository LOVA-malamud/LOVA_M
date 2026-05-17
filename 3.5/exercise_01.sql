SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

SELECT e.name, d.dept_name, d.budget
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
WHERE d.budget > 70000;

SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name;

select d.dept_name, COUNT(e.id) AS employees_count
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
GROUP BY d.dept_name
ORDER BY employees_count DESC;
SELECT region, SUM(amount) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;

SELECT product, COUNT(*) AS number_of_sales, AVG(amount) AS average_amount
FROM sales
GROUP BY product;

SELECT rep_name, SUM(amount) AS total_rep_revenue
FROM sales
GROUP BY rep_name
ORDER BY total_rep_revenue DESC;

SELECT region, rep_name, COUNT(*) AS sale_count, SUM(amount) AS total_amount
FROM sales
GROUP BY region, rep_name;

SELECT rep_name, COUNT(*) AS laptop_count
FROM sales
WHERE product = 'Laptop'
GROUP BY rep_name
ORDER BY laptop_count DESC
LIMIT 1;

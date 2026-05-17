SELECT region, sum(amount) AS total_revenue
FROM sales
GROUP BY region
HAVING total_revenue > 1500;

SELECT product, count(*) AS sales_count
FROM sales
GROUP BY product
HAVING sales_count >= 3;

select rep_name, AVG(amount) AS average_sales
from sales
group by rep_name
having average_sales > 900;

SELECT rep_name, count(*) as sales_count
FROM sales
WHERE product in ('Laptop', 'Phone') 
GROUP BY rep_name
HAVING sales_count >= 1;

SELECT
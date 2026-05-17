SELECT 
        sum(amount) AS total_revenue,
        AVG(amount) AS average_sales,
        min(amount) AS cheapest_sale,
        max(amount) AS most_expensive_sale
FROM sales;

SELECT sum(amount) AS North_total_revenue
FROM sales
WHERE region = 'North';

select max(amount) AS most_expensive_laptop_sold
from sales
where product = 'Laptop';

SELECT AVG(amount) / count(*) AS average_treating_null_as_zero
FROM sales;

SELECT
    max(sale_date) AS earliest_sale_date,
    min(sale_date) AS latest_sale_date
FROM sales;
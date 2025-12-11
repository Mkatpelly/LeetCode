# Write your MySQL query statement below
WITH ranked AS (
    SELECT
        id,
        company,
        salary,
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS row_num,
        COUNT(*) OVER (PARTITION BY company) AS total
    FROM 
        Employee
)
SELECT 
    id,
    company,
    salary
FROM 
    ranked
WHERE 
    row_num IN (FLOOR((total + 1) / 2), FLOOR((total + 2) / 2));
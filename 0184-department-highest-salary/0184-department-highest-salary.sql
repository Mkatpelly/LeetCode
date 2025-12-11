# Write your MySQL query statement below
WITH salary_ranks AS (
  SELECT 
    e.name AS Employee,
    e.salary,
    e.departmentId,
    d.name AS Department,
    RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
  FROM Employee e
  JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, salary AS Salary
FROM salary_ranks
WHERE rnk = 1;
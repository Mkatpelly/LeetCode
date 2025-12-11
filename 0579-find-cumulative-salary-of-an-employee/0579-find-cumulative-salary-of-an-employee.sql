# Write your MySQL query statement below
WITH CurrMonth AS (
  SELECT *,
         MAX(month) OVER (PARTITION BY id) AS max_month
  FROM Employee
)
SELECT c.id,
       c.month,
       SUM(p.salary) AS salary
FROM CurrMonth c
JOIN Employee p
  ON c.id = p.id
 AND c.month - p.month BETWEEN 0 AND 2
WHERE c.month != c.max_month
GROUP BY c.id, c.month
ORDER BY c.id ASC, c.month DESC;
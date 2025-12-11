WITH numbered AS (
  SELECT num,
         frequency,
         SUM(frequency) OVER (ORDER BY num) AS running_frequency,
         SUM(frequency) OVER () AS total_frequency
  FROM Numbers
)
SELECT ROUND(AVG(num * 1.0), 1) AS median
FROM numbered
WHERE total_frequency / 2.0 BETWEEN running_frequency - frequency AND running_frequency;
# Write your MySQL query statement below
WITH alldate AS (
    SELECT 
        fail_date AS date,
        'failed' AS period_state
    FROM Failed
    UNION ALL
    SELECT
        success_date AS date,
        'succeeded' AS period_state
    FROM Succeeded
),
tpos AS (
    SELECT *,
        ROW_NUMBER() OVER (ORDER BY date) -
        RANK() OVER (PARTITION BY period_state ORDER BY date) AS pos
    FROM alldate
    WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
    ORDER BY date
)
SELECT 
    period_state,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM tpos
GROUP BY pos, period_state
ORDER BY start_date;
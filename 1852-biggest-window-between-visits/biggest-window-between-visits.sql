# Write your MySQL query statement below
WITH all_dates AS(
    SELECT user_id, visit_date
    FROM UserVisits
    UNION
    SELECT user_id, '2021-01-01' AS 'visit_date'
    FROM UserVisits)
, rnk AS(
    SELECT *, 
        RANK()OVER(PARTITION BY user_id ORDER BY visit_date) AS date_rnk
    FROM all_dates
)
SELECT a.user_id, MAX(DATEDIFF(b.visit_date, a.visit_date)) AS biggest_window
FROM rnk a, rnk b
WHERE a.user_id = b.user_id
AND b.date_rnk = a.date_rnk + 1
GROUP BY a.user_id
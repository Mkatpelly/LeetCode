# Write your MySQL query statement below
WITH user_by_activity AS 
    (
    SELECT activity, COUNT(DISTINCT id) AS user_cnts
    FROM Friends
    GROUP BY activity
    )
SELECT activity
FROM user_by_activity u
LEFT JOIN 
    (SELECT MAX(user_cnts) AS user_cnts 
    FROM user_by_activity
    UNION
    SELECT MIN(user_cnts) AS user_cnts 
    FROM user_by_activity
    )m
ON u.user_cnts = m.user_cnts
WHERE m.user_cnts IS NULL
# Write your MySQL query statement below
SELECT DISTINCT a.user_id
FROM Confirmations a
JOIN Confirmations b 
  ON a.user_id = b.user_id
 AND a.time_stamp <> b.time_stamp
WHERE ABS(TIMESTAMPDIFF(SECOND, a.time_stamp, b.time_stamp)) <= 86400;
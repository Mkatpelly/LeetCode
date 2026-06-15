# Write your MySQL query statement below
SELECT school_id, MIN(IF(ISNULL(score),-1, score)) AS score 
FROM Schools
LEFT JOIN Exam
ON student_count <= capacity
GROUP BY school_id;
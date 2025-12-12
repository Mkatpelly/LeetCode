# Write your MySQL query statement below
SELECT C.name
FROM Vote AS V
JOIN Candidate AS C
ON V.candidateId = C.id
GROUP BY V.candidateId, C.name
ORDER BY COUNT(*) DESC
LIMIT 1;
# Write your MySQL query statement below
WITH AllFriends AS (
  SELECT requester_id AS id FROM RequestAccepted
  UNION ALL
  SELECT accepter_id FROM RequestAccepted
),
FriendCount AS (
  SELECT id, COUNT(*) AS num
  FROM AllFriends
  GROUP BY id
),
MaxCount AS (
  SELECT MAX(num) AS max_num FROM FriendCount
)
SELECT id, num
FROM FriendCount
WHERE num = (SELECT max_num FROM MaxCount);
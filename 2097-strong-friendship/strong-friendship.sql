# Write your MySQL query statement below
WITH TwoWayFriendship AS (
    SELECT user1_id AS user_id, user2_id AS friend_id
    FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id
    FROM Friendship
),
CommonFriends AS (
    SELECT
        LEAST(f1.user_id, f2.user_id)  AS user1_id,
        GREATEST(f1.user_id, f2.user_id) AS user2_id,
        COUNT(*) AS common_friend
    FROM TwoWayFriendship f1
    JOIN TwoWayFriendship f2
      ON f1.friend_id = f2.friend_id      -- same common friend
     AND f1.user_id < f2.user_id          -- avoid duplicate pairs
    GROUP BY
        LEAST(f1.user_id, f2.user_id),
        GREATEST(f1.user_id, f2.user_id)
)
SELECT
    c.user1_id,
    c.user2_id,
    c.common_friend
FROM CommonFriends c
JOIN Friendship f
  ON f.user1_id = c.user1_id
 AND f.user2_id = c.user2_id
WHERE c.common_friend >= 3;
# Write your MySQL query statement below
WITH PlayerScores AS (
  SELECT player_id, group_id, first_score AS score
  FROM Players
  JOIN Matches
    ON player_id = first_player
  UNION ALL
  SELECT player_id, group_id, second_score AS score
  FROM Players
  JOIN Matches
    ON player_id = second_player
),
TotalScores AS (
  SELECT
    group_id,
    player_id,
    SUM(score) AS total_score
  FROM PlayerScores
  GROUP BY group_id, player_id
),
Ranked AS (
  SELECT
    group_id,
    player_id,
    RANK() OVER (
      PARTITION BY group_id
      ORDER BY total_score DESC, player_id ASC
    ) AS rnk
  FROM TotalScores
)
SELECT group_id, player_id
FROM Ranked
WHERE rnk = 1;
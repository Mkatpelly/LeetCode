# Write your MySQL query statement below
WITH UserToAmount AS (
  SELECT 
    user_id,
    spend_date,
    CASE 
      WHEN COUNT(DISTINCT platform) = 2 THEN 'both'
      ELSE MAX(platform)
    END AS platform,
    SUM(amount) AS amount
  FROM Spending
  GROUP BY user_id, spend_date
),
DateAndPlatforms AS (
  SELECT DISTINCT spend_date, 'desktop' AS platform FROM Spending
  UNION ALL
  SELECT DISTINCT spend_date, 'mobile' FROM Spending
  UNION ALL
  SELECT DISTINCT spend_date, 'both' FROM Spending
)
SELECT 
  d.spend_date,
  d.platform,
  COALESCE(SUM(u.amount), 0) AS total_amount,
  COALESCE(COUNT(DISTINCT u.user_id), 0) AS total_users
FROM DateAndPlatforms d
LEFT JOIN UserToAmount u
  ON d.spend_date = u.spend_date
  AND d.platform = u.platform
GROUP BY d.spend_date, d.platform;

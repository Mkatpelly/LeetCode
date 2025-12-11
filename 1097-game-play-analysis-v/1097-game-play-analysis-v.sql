# Write your MySQL query statement below
WITH FirstInstall AS (
    SELECT 
        player_id,
        MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
)
SELECT 
    f.install_dt,
    COUNT(f.player_id) AS installs,
    ROUND(COUNT(a.player_id) / COUNT(f.player_id), 2) AS Day1_retention
FROM FirstInstall f
LEFT JOIN Activity a
    ON f.player_id = a.player_id 
    AND a.event_date = DATE_ADD(f.install_dt, INTERVAL 1 DAY)
GROUP BY f.install_dt;
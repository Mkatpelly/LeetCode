# Write your MySQL query statement below
WITH RankedSales AS (
  SELECT 
    o.seller_id,
    i.item_brand,
    RANK() OVER (PARTITION BY o.seller_id ORDER BY o.order_date) AS sale_rank
  FROM Orders o
  JOIN Items i 
    ON o.item_id = i.item_id
)
SELECT 
  u.user_id AS seller_id,
  CASE 
    WHEN r.item_brand = u.favorite_brand THEN 'yes'
    ELSE 'no'
  END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN RankedSales r
  ON u.user_id = r.seller_id
  AND r.sale_rank = 2;
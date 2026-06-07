# Write your MySQL query statement below
SELECT c.customer_id, c.name
  FROM Orders o
  JOIN Product p
    ON o.product_id = p.product_id
  JOIN Customers c
    ON o.customer_id = c.customer_id
 GROUP BY o.customer_id
HAVING SUM(CASE WHEN YEAR(order_date)=2020 AND MONTH(order_date) = 06 THEN quantity*price END) >= 100
   AND SUM(CASE WHEN YEAR(order_date)=2020 AND MONTH(order_date) = 07 THEN quantity*price END) >= 100
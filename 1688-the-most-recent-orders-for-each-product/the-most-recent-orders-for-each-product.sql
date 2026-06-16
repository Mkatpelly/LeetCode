# Write your MySQL query statement below
select b.product_name, a.product_id, a.order_id, a.order_date from Orders a
join Products b
on a.product_id = b.product_id
where (a.product_id, a.order_date) in (
select product_id, max(order_date) as order_date
from Orders
group by product_id)
order by b.product_name, a.product_id, a.order_id
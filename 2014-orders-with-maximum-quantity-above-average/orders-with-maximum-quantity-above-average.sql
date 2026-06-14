# Write your MySQL query statement below
with cte as (
    select order_id,
    max(avg(quantity)) over() as max_avg_qty,
    max(quantity) as max_qty
    from ordersdetails
    group by order_id
)
select order_id from cte where max_qty>max_avg_qty
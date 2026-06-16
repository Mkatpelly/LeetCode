# Write your MySQL query statement below

select
    product_name, product_id, order_id, order_date
from
    Orders
    join
    Products
    using (product_id)
where (product_id, order_date) in
    (select
        product_id, max(order_date) as order_date
    from
        Orders
    group by
        product_id)
order by
    product_name, product_id, order_id
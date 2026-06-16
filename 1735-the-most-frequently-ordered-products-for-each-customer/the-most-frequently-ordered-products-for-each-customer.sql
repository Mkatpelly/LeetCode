# Write your MySQL query statement below

with t as (
    select 
        customer_id, 
        product_id, 
        count(*) as c 
    from orders 
    group by customer_id, product_id
), 

t1 as (
    select 
        customer_id, 
        max(c) as mx
    from t
    group by customer_id
), 

t2 as (
    select 
        t.customer_id, 
        product_id
    from t
    join t1
    on t.customer_id = t1.customer_id
    where c = mx
)

select 
    customer_id, 
    t2.product_id, 
    product_name 
from t2 
join products as p
on t2.product_id = p.product_id 





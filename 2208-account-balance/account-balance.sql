# Write your MySQL query statement below
select t1.account_id ,t1.day ,sum(case when t2.type='Deposit' then t2.amount else -1*t2.amount end) as balance 
from transactions t1 ,transactions t2 
where t1.account_id =t2.account_id and t1.day>=t2.day 
group by t1.account_id ,t1.day 
order by account_id asc ,day asc
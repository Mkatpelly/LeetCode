# Write your MySQL query statement below
with recursive months as(
    select 1 as month
    union all
    select month+1
    from months
    where month<12
),
available_drivers as(
    select driver_id,
    case when year(join_date)<2020 then 1
    else month(join_date) end available_month
    from drivers
    where year(join_date)<2021
),
available_drivers_per_month as(
    select month,
    count(driver_id) total_driver
    from months
    left join available_drivers
    on month>=available_month
    group by 1
),
drivers_with_acc_rides_per_month as(
    select distinct driver_id,month(requested_at ) accept_month
from AcceptedRides 
left join Rides 
using(ride_id)
where year(requested_at)=2020
)
select month,
case when total_driver=0 then 0.00
else round(count(distinct driver_id ) /(total_driver) *100.0 ,2) end working_percentage 
from available_drivers_per_month
left join drivers_with_acc_rides_per_month
on month=accept_month
group by 1
order by 1
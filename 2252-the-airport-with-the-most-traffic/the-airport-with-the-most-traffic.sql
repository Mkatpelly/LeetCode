# Write your MySQL query statement below
with all_flights as (
    select departure_airport as airport_id,
        flights_count as flights_cnt
    from Flights

    union all

    select arrival_airport as airport_id,
        flights_count as flights_cnt
    from Flights
), airport_ranks as (
    select airport_id,
        rank() over(order by sum(flights_cnt) desc) as rnk
    from all_flights
    group by airport_id
)
select airport_id
from airport_ranks
where rnk = 1;
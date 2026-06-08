# Write your MySQL query statement below
select username, activity, startDate, endDate
from (
select *, count(activity) over(partition by username)cnt, 
ROW_NUMBER() over(partition by username order by startdate desc) n from UserActivity) tbl
where n=2 or cnt<2
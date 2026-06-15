# Write your MySQL query statement below
with is_min_max as (
    select 
        student_id,
        case
        when min(score) over (partition by exam_id) = score then 0
        when max(score) over (partition by exam_id) = score then 0
        else 1
        end as quiet
    from exam
)
select 
    student_id, 
    student_name
from student
where
    student_id in (select student_id from exam) and
    student_id not in (select student_id from is_min_max where quiet = 0)
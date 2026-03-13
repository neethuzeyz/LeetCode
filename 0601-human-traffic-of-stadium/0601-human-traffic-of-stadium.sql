-- Write your PostgreSQL query statement below
WITH reduced_rows AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
)

select id, visit_date, people
from reduced_rows
where grp in (
    select grp
    from reduced_rows
    group by grp
    having count(*) >= 3
)
order by visit_date;
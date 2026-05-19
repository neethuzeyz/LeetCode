-- Write your PostgreSQL query statement below
select max(num) as num
from (
    select num
    from Mynumbers
    group by num
    having count (num) =1
);
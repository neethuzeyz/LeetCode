-- Write your PostgreSQL query statement below
with all_ids as (
   select requester_id as id 
   from RequestAccepted
   union all
   select accepter_id as id
   from RequestAccepted)
select id, num
from 
   (
   select id, 
      count(id) as num, 
      rank() over(order by  count(id) desc) as rnk
   from all_ids
   group by id
   )t0
where rnk=1
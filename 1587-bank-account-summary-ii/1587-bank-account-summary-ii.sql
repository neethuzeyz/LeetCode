-- Write your PostgreSQL query statement below
select u.name,sum(t.amount) as balance
from users u
 inner join transactions t
 on t.account =u.account
 group by u.name,u.account
 having sum(t.amount)>10000
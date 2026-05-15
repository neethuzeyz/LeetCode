-- Write your PostgreSQL query statement belSE 
select tweet_id
from tweets
where length(content)>15;
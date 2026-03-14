select e.name,b.bonus
from employee e
left join  bonus b
on e.empId = b.empID
where b.bonus is null
or b.bonus < 1000;
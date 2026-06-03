select max(salary) secondhighestsalary
from employee
where salary <(select max(salary)from employee);
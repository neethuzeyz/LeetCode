select eu.unique_id,e.name
from employees e
left join employeeUni eu
on eu.id= e.id;
 
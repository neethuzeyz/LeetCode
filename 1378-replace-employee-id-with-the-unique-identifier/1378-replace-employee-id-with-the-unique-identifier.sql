select EmployeeUNI.unique_id, employees.name
from employees
left join employeeUNI on Employees.id = EmployeeUNI.id
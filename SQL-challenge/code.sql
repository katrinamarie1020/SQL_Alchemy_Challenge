-- List the following details of each employee: employee number, last name, first name, sex, and salary.
select e.emp_no, e.last_name, e.first_name, e.sex, s.salary
from "Employees" as e 
inner join
salaries as s on 
e.emp_no = s.emp_no;

-- List first name, last name, and hire date for employees who were hired in 1986.
select first_name, last_name, hire_date 
from "Employees" 
where hire_date >= '1986-01-01'
and hire_date < '1987-01-01';

-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

select dm.emp_no, dm.dept_no, d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name
FROM dept_manager dm
LEFT JOIN departments d
ON dm.dept_no = d.dept_no
LEFT JOIN "Employees" e
ON e.emp_no = dm.emp_no;

-- List the department of each employee with the following information: employee number, last name, first name, and department name.
select de.emp_no, de.dept_no, d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name
FROM dept_employee de
LEFT JOIN departments d
ON de.dept_no = d.dept_no
LEFT JOIN "Employees" e
ON e.emp_no = de.emp_no;

-- List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select sex, first_name, last_name from "Employees" where
first_name = 'Hercules' and
last_name like 'B%';

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.

select de.emp_no, de.dept_no, d.dept_name, e.last_name, e.first_name
FROM dept_employee de
LEFT JOIN departments d
ON de.dept_no = d.dept_no
LEFT JOIN "Employees" e
ON e.emp_no = de.emp_no
where dept_name = 'Sales';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select count(last_name), last_name
from "Employees"
group by last_name
order by count(last_name) desc



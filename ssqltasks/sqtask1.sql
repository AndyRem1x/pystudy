SELECT
  employees.first_name,
  employees.last_name,
  employees.department_id,
  departments.depart_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;

SELECT
  employees.first_name,
  employees.last_name,
  employees.department_id,
  departments.depart_name,
  locations.city,
  locations.state_province
FROM employees
LEFT JOIN departments USING(department_id)
LEFT JOIN locations USING(location_id);

SELECT
  employees.first_name,
  employees.last_name,
  employees.department_id,
  departments.depart_name
FROM employees
LEFT JOIN departments USING(department_id)
WHERE employees.department_id = 40 OR employees.department_id = 80;

SELECT * FROM departments

SELECT
  empl_1.first_name AS 'Employee first name',
  COALESCE(empl_2.first_name, NULL) AS 'Manager first name'
FROM employees AS empl_1
LEFT JOIN employees AS empl_2
ON empl_1.manager_id = empl_2.employee_id;

SELECT
  jobs.job_title,
  employees.first_name || ' ' || employees.last_name AS 'employee_full_name',
  (jobs.max_salary - employees.salary) AS dif_salary
FROM employees
LEFT JOIN jobs USING (job_id);

SELECT
  jobs.job_title,
  AVG(employees.salary) AS 'average salary'
FROM jobs
INNER JOIN employees USING (job_id)
GROUP BY jobs.job_title;

SELECT
  employees.first_name || ' ' || employees.last_name AS 'employee_full_name',
  locations.city AS 'department_city'
FROM employees
LEFT JOIN departments USING(department_id)
LEFT JOIN locations USING(location_id)
WHERE locations.city = 'London';

SELECT
  employees.first_name || ' ' || employees.last_name AS 'employee_full_name',
  employees.salary,
  locations.city AS 'department_city'
FROM employees
LEFT JOIN departments USING(department_id)
LEFT JOIN locations USING(location_id)
WHERE locations.city = 'London';
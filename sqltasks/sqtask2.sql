SELECT first_name AS 'First name', last_name AS 'Last name' FROM employees;
SELECT DISTINCT department_id FROM employees;
SELECT * FROM employees ORDER BY last_name DESC, first_name DESC;
SELECT first_name, last_name, salary, salary * 0.12 AS PF FROM employees;
SELECT MAX(salary) AS 'Salary (max)', MIN(salary) AS 'Salary (min)' FROM employees;
SELECT first_name, last_name, ROUND(salary, 2) AS 'monthly_salary' FROM employees;
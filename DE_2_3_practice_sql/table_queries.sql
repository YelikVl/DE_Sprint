-- Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании
SELECT emp_id, full_name, EXTRACT(YEAR FROM current_date)-EXTRACT(YEAR from start_date) AS years_employed
FROM employees;

--  Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников

SELECT emp_id, full_name, EXTRACT(YEAR FROM current_date)-EXTRACT(YEAR from start_date) AS years_employed
FROM employees
ORDER BY years_employed DESC
LIMIT 3;

-- Уникальный номер сотрудников - водителей
SELECT emp_id
FROM employees
WHERE job_title = 'DRIVER';

-- Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E

SELECT DISTINCT emp_id from bonus_grades WHERE grade IN ('D', 'E');


--Выведите самую высокую зарплату в компании.

SELECT MAX(salary) AS MAX_salary
from employees;

--* Выведите название самого крупного отдела
SELECT dep_name from departments
WHERE num_employees = (SELECT MAX(num_employees) FROM departments);

--  * Выведите номера сотрудников от самых опытных до вновь прибывших
SELECT emp_id FROM (SELECT emp_id, full_name, EXTRACT(YEAR FROM current_date)-EXTRACT(YEAR from start_date) AS years_employed
FROM employees
ORDER BY years_employed DESC) AS employees_by_exp;

-- * Рассчитайте среднюю зарплату для каждого уровня сотрудников
SELECT grade_level, AVG(SALARY) as average_salary
FROM employees
group by grade_level;

-- * Добавьте столбец с информацией о коэффициенте годовой премии к основной --таблице. Коэффициент рассчитывается по такой схеме: базовое значение коэффициента – --1, каждая оценка действует на коэффициент так:
--
--·         Е – минус 20%
--
--·         D – минус 10%
--
--·         С – без изменений
--
--·         B – плюс 10%
--
--·         A – плюс 20%
--
--Соответственно, сотрудник с оценками А, В, С, D – должен получить коэффициент 1.2.

CREATE TABLE IF NOT EXISTS public.bonus_coefs AS(
SELECT emp_id, sum(COEF)+1 as bonus_coef
FROM (
SELECT bonus_grades.emp_id, bonus_grades.grade, COUNT (grade) as grade_count,
       CASE WHEN bonus_grades.grade = 'A' then 0.2
	   		WHEN bonus_grades.grade = 'B' then 0.1
			WHEN bonus_grades.grade = 'D' then -0.1
			WHEN bonus_grades.grade = 'E' then -0.2
			ELSE 0.0
	   END AS COEF	
FROM bonus_grades
WHERE bonus_grades.emp_id IN
      (SELECT bonus_grades.emp_id
	   FROM bonus_grades, employees
	   WHERE (bonus_grades.emp_id = employees.emp_id)) AND bonus_grades."year"=2021
GROUP BY bonus_grades.emp_id, bonus_grades.grade) as ss
GROUP BY emp_id);

SELECT * FROM employees e
LEFT join bonus_coefs bc 
ON e.emp_id = bc.emp_id;


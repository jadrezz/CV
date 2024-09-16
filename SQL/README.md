# Решение задач с сайта [SQL Academy](https://sql-academy.org/)
## [Сертификат об успешном освоении курса по SQL](./certificate.pdf)


### Ниже предоставляю свои решения упражнений



1. [Вывести имена всех людей, которые есть в базе данных авиакомпаний](https://sql-academy.org/ru/trainer/tasks/1)

<details>
  <summary>Решение</summary>

```SQL
SELECT name
FROM Passenger
```
</details>

2. [Вывести названия всеx авиакомпаний](https://sql-academy.org/ru/trainer/tasks/2)

<details>
  <summary>Решение</summary>

```SQL
SELECT name
FROM Company;
```
</details>

3. [Вывести все рейсы, совершенные из Москвы
](https://sql-academy.org/ru/trainer/tasks/3)

<details>
  <summary>Решение</summary>

```SQL
SELECT *
FROM Trip
WHERE town_from = 'Moscow';
```
</details>


4. [Вывести имена людей, которые заканчиваются на "man"](https://sql-academy.org/ru/trainer/tasks/4)

<details>
  <summary>Решение</summary>

```SQL
SELECT name
FROM Passenger
WHERE name LIKE '%man';
```
</details>


5. [Вывести количество рейсов, совершенных на TU-134](https://sql-academy.org/ru/trainer/tasks/5)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(*) AS count
FROM Trip
WHERE plane = 'TU-134';
```
</details>


6. [Какие компании совершали перелеты на Boeing](https://sql-academy.org/ru/trainer/tasks/6)

<details>
  <summary>Решение</summary>

```SQL
SELECT Company.name AS name
FROM Company
WHERE Company.id IN (
		SELECT DISTINCT company
		FROM Trip
		WHERE plane = 'Boeing'
	)
```
</details>

7. [Вывести все названия самолётов, на которых можно улететь в Москву (Moscow)](https://sql-academy.org/ru/trainer/tasks/7)

<details>
  <summary>Решение</summary>

```SQL
SELECT DISTINCT plane
FROM Trip
WHERE town_to = 'Moscow'
```
</details>

8. [В какие города можно улететь из Парижа (Paris) и сколько времени это займёт?](https://sql-academy.org/ru/trainer/tasks/8)

<details>
  <summary>Решение</summary>

```SQL
SELECT town_to,
	CAST(time_in - time_out AS time) AS flight_time
FROM trip
WHERE town_from = 'Paris'
```
</details>

9. [Какие компании организуют перелеты из Владивостока (Vladivostok)?](https://sql-academy.org/ru/trainer/tasks/9)

<details>
  <summary>Решение</summary>

```SQL  
SELECT DISTINCT name
FROM Company
WHERE Company.id IN (
		SELECT DISTINCT company
		FROM Trip
		WHERE town_from = 'Vladivostok'
	)
```
</details>

10. [Вывести вылеты, совершенные с 10 ч. по 14 ч. 1 января 1900 г.](https://sql-academy.org/ru/trainer/tasks/10)

<details>
  <summary>Решение</summary>

```SQL
SELECT *
FROM Trip
WHERE time_out BETWEEN '1900-01-01T10:00:00' AND '1900-01-01T14:00:00'
```
</details>

11. [Выведите пассажиров с самым длинным ФИО. Пробелы, дефисы и точки считаются частью имени.](https://sql-academy.org/ru/trainer/tasks/11)

<details>
  <summary>Решение</summary>

```SQL
SELECT name
FROM passenger
WHERE LENGTH(name) = (
		SELECT MAX(LENGTH(name))
		FROM Passenger
	)
```
</details>

12. [Вывести id и количество пассажиров для всех прошедших полётов](https://sql-academy.org/ru/trainer/tasks/12)

<details>
  <summary>Решение</summary>

```SQL
SELECT trip,
	COUNT(passenger) AS count
FROM Pass_in_trip
GROUP BY trip
```
</details>

13. [Вывести имена людей, у которых есть полный тёзка среди пассажиров](https://sql-academy.org/ru/trainer/tasks/13)

<details>
  <summary>Решение</summary>

```SQL
SELECT name
FROM Passenger
GROUP BY name
HAVING COUNT(*) > 1
```
</details>

14. [В какие города летал Bruce Willis
](https://sql-academy.org/ru/trainer/tasks/14)

<details>
  <summary>Решение</summary>

```SQL
SELECT town_to
FROM trip
	INNER JOIN Pass_in_trip ON Trip.id = Pass_in_trip.trip
	INNER JOIN Passenger ON Pass_in_trip.passenger = passenger.id
WHERE passenger.name = 'Bruce Willis'
```
</details>

15. [Выведите дату и время прилёта пассажира Стив Мартин (Steve Martin) в Лондон (London)
](https://sql-academy.org/ru/trainer/tasks/15)

<details>
  <summary>Решение</summary>

```SQL
SELECT time_in
FROM trip
	INNER JOIN Pass_in_trip ON Trip.id = Pass_in_trip.trip
	INNER JOIN Passenger ON passenger = Passenger.id
WHERE name = 'Steve Martin'
	AND town_to = 'London'
```
</details>

16. [Вывести отсортированный по количеству перелетов (по убыванию) и имени (по возрастанию) список пассажиров, совершивших хотя бы 1 полет.](https://sql-academy.org/ru/trainer/tasks/16)

<details>
  <summary>Решение</summary>

```SQL
SELECT p.name AS name,
	count(*) AS count
FROM Passenger AS p
	INNER JOIN Pass_in_trip ON Pass_in_trip.passenger = p.id
GROUP BY p.name
ORDER BY count DESC,
	p.name
```
</details>

17. [Определить, сколько потратил в 2005 году каждый из членов семьи. В результирующей выборке не выводите тех членов семьи, которые ничего не потратили.](https://sql-academy.org/ru/trainer/tasks/17)

<details>
  <summary>Решение</summary>

```SQL
SELECT fm.member_name,
	fm.status,
	SUM(unit_price * amount) AS costs
FROM FamilyMembers AS fm
	INNER JOIN Payments ON fm.member_id = Payments.family_member
WHERE YEAR(date) = 2005
GROUP BY fm.member_name,
	fm.status
HAVING costs > 0
```
</details>

18. [Выведите имя самого старшего человека. Если таких несколько, то выведите их всех.](https://sql-academy.org/ru/trainer/tasks/18)

<details>
  <summary>Решение</summary>

```SQL
SELECT member_name
FROM FamilyMembers
WHERE YEAR(birthday) = (
		SELECT MIN(YEAR(birthday))
		FROM FamilyMembers
	)
```
</details>

19. [Определить, кто из членов семьи покупал картошку (potato)](https://sql-academy.org/ru/trainer/tasks/19)

<details>
  <summary>Решение</summary>

```SQL
SELECT DISTINCT status
FROM FamilyMembers
	INNER JOIN Payments ON FamilyMembers.member_id = Payments.family_member
	INNER JOIN Goods ON Payments.good = Goods.good_id
WHERE good_name = 'potato'
```
</details>

20. [Сколько и кто из семьи потратил на развлечения (entertainment). Вывести статус в семье, имя, сумму](https://sql-academy.org/ru/trainer/tasks/20)

<details>
  <summary>Решение</summary>

```SQL
SELECT status,
	member_name,
	SUM(amount * unit_price) AS costs
FROM FamilyMembers
	INNER JOIN Payments ON FamilyMembers.member_id = Payments.family_member
WHERE Payments.good IN (
		SELECT good_id
		FROM Goods
			INNER JOIN GoodTypes ON Goods.type = GoodTypes.good_type_id
		WHERE good_type_name = 'entertainment'
	)
GROUP BY status,
	member_name
```
</details>


21.  [Определить товары, которые покупали более 1 раза
](https://sql-academy.org/ru/trainer/tasks/21)

<details>
  <summary>Решение</summary>

```SQL
SELECT good_name
FROM Goods
WHERE good_id IN (
		SELECT good
		FROM Payments
		GROUP BY good
		HAVING count(good) > 1
	)
```
</details>

22. [Найти имена всех матерей (mother)
](https://sql-academy.org/ru/trainer/tasks/22)

<details>
  <summary>Решение</summary>

```SQL
SELECT member_name
FROM FamilyMembers
WHERE status = 'mother'
```
</details>

23. [Найдите самый дорогой деликатес (delicacies) и выведите его цену
](https://sql-academy.org/ru/trainer/tasks/23)

<details>
  <summary>Решение</summary>

```SQL
SELECT good_name,
	unit_price
FROM Goods
	INNER JOIN GoodTypes ON Goods.type = GoodTypes.good_type_id
	AND good_type_name = 'delicacies'
	INNER JOIN Payments ON Goods.good_id = Payments.good
WHERE unit_price = (
		SELECT max(unit_price)
		FROM Payments
			INNER JOIN Goods ON good = good_id
			INNER JOIN GoodTypes ON type = good_type_id
			AND good_type_name = 'delicacies'
	)
```
</details>

24. [Определить кто и сколько потратил в июне 2005
](https://sql-academy.org/ru/trainer/tasks/24)

<details>
  <summary>Решение</summary>

```SQL
SELECT member_name,
	SUM(unit_price * amount) AS costs
FROM FamilyMembers
	INNER JOIN Payments ON member_id = family_member
WHERE EXTRACT(
		MONTH
		FROM Payments.date
	) = 6
	AND EXTRACT(
		YEAR
		FROM Payments.date
	) = '2005'
GROUP BY member_name
```
</details>

25.  [Определить, какие товары не покупались в 2005 году
](https://sql-academy.org/ru/trainer/tasks/25)

<details>
  <summary>Решение</summary>

```SQL
SELECT good_name
FROM Goods
WHERE good_id NOT IN (
		SELECT good
		FROM Payments
		WHERE YEAR(date) = '2005'
	)
```
</details>

26. [Определить группы товаров, которые не приобретались в 2005 году](https://sql-academy.org/ru/trainer/tasks/26)

<details>
  <summary>Решение</summary>

```SQL
SELECT good_type_name FROM GoodTypes
WHERE good_type_id NOT IN 
      (SELECT DISTINCT type FROM Goods JOIN Payments ON good=good_id WHERE YEAR(date) = 2005)
```
</details>

27. [Узнайте, сколько было потрачено на каждую из групп товаров в 2005 году. Выведите название группы и потраченную на неё сумму. Если потраченная сумма равна нулю, т.е. товары из этой группы не покупались в 2005 году, то не выводите её.](https://sql-academy.org/ru/trainer/tasks/27)

<details>
  <summary>Решение</summary>

```SQL
SELECT good_type_name, SUM(amount*unit_price) AS costs FROM GoodTypes
JOIN Goods ON good_type_id=type
JOIN Payments ON good_id=good
WHERE YEAR(date) = 2005
GROUP BY good_type_name
HAVING costs > 0
```
</details>

28. [Сколько рейсов совершили авиакомпании из Ростова (Rostov) в Москву (Moscow) ?](https://sql-academy.org/ru/trainer/tasks/18)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(*) AS count
FROM Trip
WHERE Trip.town_from = 'Rostov'
	AND Trip.town_to = 'Moscow'
```
</details>

29. [Выведите имена пассажиров улетевших в Москву (Moscow) на самолете TU-134](https://sql-academy.org/ru/trainer/tasks/29)

<details>
  <summary>Решение</summary>

```SQL
SELECT DISTINCT name
FROM Passenger
	INNER JOIN Pass_in_trip ON Passenger.id = Pass_in_trip.passenger
	INNER JOIN Trip ON Pass_in_trip.trip = Trip.id
WHERE town_to = 'Moscow'
	AND plane = 'TU-134'
```
</details>

30. [Выведите нагруженность (число пассажиров) каждого рейса (trip). Результат вывести в отсортированном виде по убыванию нагруженности.](https://sql-academy.org/ru/trainer/tasks/30)

<details>
  <summary>Решение</summary>

```SQL
SELECT trip,
	count(*) AS count
FROM Pass_in_trip
GROUP BY trip
ORDER BY count DESC
```
</details>


31. [Вывести всех членов семьи с фамилией Quincey.](https://sql-academy.org/ru/trainer/tasks/31)

<details>
  <summary>Решение</summary>

```SQL
SELECT *
FROM FamilyMembers
WHERE member_name LIKE '%Quincey'
```
</details>

32. [Вывести средний возраст людей (в годах), хранящихся в базе данных. Результат округлите до целого в меньшую сторону.](https://sql-academy.org/ru/trainer/tasks/32)

<details>
  <summary>Решение</summary>

```SQL
SELECT round(avg(YEAR(current_date) - YEAR(birthday))) as age
FROM FamilyMembers
```
</details>

33. [Найдите среднюю цену икры на основе данных, хранящихся в таблице Payments. В базе данных хранятся данные о покупках красной (red caviar) и черной икры (black caviar). В ответе должна быть одна строка со средней ценой всей купленной когда-либо икры.](https://sql-academy.org/ru/trainer/tasks/33)

<details>
  <summary>Решение</summary>

```SQL
SELECT AVG(unit_price) AS cost
FROM Payments
	INNER JOIN Goods ON Payments.good = Goods.good_id
WHERE Goods.good_name LIKE '%caviar'
```
</details>

34. [Сколько всего 10-ых классов](https://sql-academy.org/ru/trainer/tasks/34)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(*) as count
FROM Class
WHERE name LIKE '%10%'
```
</details>

35. [Сколько различных кабинетов школы использовались 2 сентября 2019 года для проведения занятий?](https://sql-academy.org/ru/trainer/tasks/35)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(DISTINCT classroom) as count
FROM Schedule
WHERE Schedule.date = '2019.09.02'
```
</details>

36. [Выведите информацию об обучающихся живущих на улице Пушкина (ul. Pushkina)?](https://sql-academy.org/ru/trainer/tasks/36)

<details>
  <summary>Решение</summary>

```SQL
SELECT *
FROM Student
WHERE address LIKE '%ul. Pushkina%'
```
</details>

37. [Сколько лет самому молодому обучающемуся ?](https://sql-academy.org/ru/trainer/tasks/37)

<details>
  <summary>Решение</summary>

```SQL
SELECT ROUND(MIN(DATEDIFF(NOW(), birthday) / 365)) AS year
FROM Student
```
</details>

38. [Сколько Анн (Anna) учится в школе ?](https://sql-academy.org/ru/trainer/tasks/38)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(*) AS count
FROM Student
WHERE first_name LIKE 'Anna%'
```
</details>

39. [Сколько обучающихся в 10 B классе ?](https://sql-academy.org/ru/trainer/tasks/39)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(*) as count
FROM Student_in_class
WHERE class = (
		SELECT id
		FROM Class
		WHERE name = '10 B'
	)
```
</details>


40. [Выведите название предметов, которые преподает Ромашкин П.П. (Romashkin P.P.). Обратите внимание, что в базе данных есть несколько учителей с такими фамилией и инициалами.](https://sql-academy.org/ru/trainer/tasks/40)

<details>
  <summary>Решение</summary>

```SQL
SELECT name as subjects
FROM Subject
	INNER JOIN Schedule ON subject.id = Schedule.subject
	INNER JOIN Teacher ON Schedule.teacher = teacher.id
WHERE Teacher.last_name = 'Romashkin'
	AND Teacher.first_name LIKE 'P%'
	AND Teacher.middle_name LIKE 'P%'
```
</details>

41. [Выясните, во сколько по расписанию начинается четвёртое занятие.](https://sql-academy.org/ru/trainer/tasks/41)

<details>
  <summary>Решение</summary>

```SQL
SELECT start_pair
FROM Timepair
LIMIT 1 OFFSET 3
```
</details>

42. [Сколько времени обучающийся будет находиться в школе, учась со 2-го по 4-ый уч. предмет?](https://sql-academy.org/ru/trainer/tasks/42)

<details>
  <summary>Решение</summary>

```SQL
SELECT CAST(
		(
			SELECT end_pair
			FROM Timepair
			WHERE id = 4
		) - (
			SELECT start_pair
			from Timepair
			where id = 2
		) AS TIME
	) AS time
```
</details>


43. [Выведите фамилии преподавателей, которые ведут физическую культуру (Physical Culture). Отсортируйте преподавателей по фамилии в алфавитном порядке.](https://sql-academy.org/ru/trainer/tasks/43)

<details>
  <summary>Решение</summary>

```SQL
SELECT last_name
FROM Teacher
	INNER JOIN Schedule ON teacher.id = Schedule.teacher
	INNER JOIN Subject ON Schedule.subject = Subject.id
WHERE subject.name = 'Physical Culture'
ORDER BY last_name
```
</details>


44. [Найдите максимальный возраст (количество лет) среди обучающихся 10 классов на сегодняшний день. Для получения текущих даты и времени используйте функцию NOW().](https://sql-academy.org/ru/trainer/tasks/44)

<details>
  <summary>Решение</summary>

```SQL
SELECT (YEAR(NOW()) - MIN(YEAR(birthday))) as max_year
FROM Student
	INNER JOIN Student_in_class ON Student.id = Student_in_class.student
	INNER JOIN Class ON Class.id = Student_in_class.class
WHERE Class.name LIKE '10%'
```
</details>


45. [Какие кабинеты чаще всего использовались для проведения занятий? Выведите те, которые использовались максимальное количество раз.](https://sql-academy.org/ru/trainer/tasks/45)

<details>
  <summary>Решение</summary>

```SQL
WITH maximum AS (
	SELECT classroom,
		COUNT(classroom) AS total
	FROM Schedule
	GROUP BY classroom
)
SELECT classroom
FROM maximum
WHERE total = (
		SELECT MAX(total)
		FROM maximum
	);
```
</details>


46. [В каких классах введет занятия преподаватель "Krauze" ?](https://sql-academy.org/ru/trainer/tasks/46)

<details>
  <summary>Решение</summary>

```SQL
SELECT DISTINCT name
FROM class
	INNER JOIN Schedule ON class.id = Schedule.class
WHERE teacher = (
		SELECT id
		FROM Teacher
		WHERE last_name = 'Krauze'
	)
```
</details>


47. [Сколько занятий провел Krauze 30 августа 2019 г.?](https://sql-academy.org/ru/trainer/tasks/47)

<details>
  <summary>Решение</summary>

```SQL
SELECT count(*) as count
FROM Schedule
WHERE teacher = (
		SELECT id
		FROM Teacher
		WHERE last_name = 'Krauze'
	)
	AND date = '2019-08-30'
```
</details>


48. [Выведите заполненность классов в порядке убывания](https://sql-academy.org/ru/trainer/tasks/48)

<details>
  <summary>Решение</summary>

```SQL
SELECT name,
	count(*) as count
FROM Class
	INNER JOIN Student_in_class ON Class.id = class
GROUP BY name
ORDER BY count DESC
```
</details>


49. [Какой процент обучающихся учится в "10 A" классе? Выведите ответ в диапазоне от 0 до 100 с округлением до четырёх знаков после запятой, например, 96.0201.](https://sql-academy.org/ru/trainer/tasks/49)

<details>
  <summary>Решение</summary>

```SQL
WITH StudentsTotal AS 
(SELECT count(*) AS total FROM Student_in_class),
ParticularClass AS (
SELECT count(*) FROM Student_in_class INNER JOIN Class
ON Student_in_class.class=Class.id WHERE Class.name = '10 A'
)


SELECT ROUND(((SELECT * FROM ParticularClass) / (SELECT * FROM StudentsTotal) * 100), 4) AS percent
```
</details>


50. [Какой процент обучающихся родился в 2000 году? Результат округлить до целого в меньшую сторону.](https://sql-academy.org/ru/trainer/tasks/50)

<details>
  <summary>Решение</summary>

```SQL
WITH TotalStudents AS 
(SELECT count(*) FROM Student),
ParticularStudents AS
(SELECT count(*) FROM Student WHERE YEAR(birthday) = 2000)

SELECT FLOOR((((SELECT * FROM ParticularStudents) / (SELECT * FROM TotalStudents) * 100))) AS percent
```
</details>

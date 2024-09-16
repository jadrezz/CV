# Продолжение решения некоторых задач с сайта SQL-Academy

64. [Вывести количество бронирований по каждому месяцу каждого года, в которых было хотя бы 1 бронирование. Результат отсортируйте в порядке возрастания даты бронирования.](https://sql-academy.org/ru/trainer/tasks/64)

<details>
  <summary>Решение</summary>

```SQL
SELECT EXTRACT(
		YEAR
		FROM start_date
	) AS year,
	EXTRACT(
		MONTH
		FROM start_date
	) AS month,
	count(*) AS amount
FROM Reservations
GROUP BY YEAR,
	MONTH
ORDER BY YEAR
```
</details>

65. [Необходимо вывести рейтинг для комнат, которые хоть раз арендовали, как среднее значение рейтинга отзывов округленное до целого вниз.](https://sql-academy.org/ru/trainer/tasks/65)

<details>
  <summary>Решение</summary>

```SQL
SELECT room_id,
	floor(AVG(rating)) AS rating
FROM Reservations
	INNER JOIN Reviews ON Reservations.id = Reviews.reservation_id
GROUP BY room_id
```
</details>

93. [Какой средний возраст клиентов, купивших Smartwatch (использовать наименование товара product.name) в 2024 году?](https://sql-academy.org/ru/trainer/tasks/93)

<details>
  <summary>Решение</summary>

```SQL
SELECT AVG(customers.age) AS average_age
FROM (
		SELECT DISTINCT Customer.customer_key,
			Customer.age
		FROM Purchase
			JOIN Customer ON Purchase.customer_key = Customer.customer_key
			JOIN Product ON Purchase.product_key = Product.product_key
		WHERE Product.name = 'Smartwatch'
			AND YEAR(Purchase.date) = 2024
	) AS customers
```
</details>

99. [Посчитай доход с женской аудитории (доход = сумма(price * items)). Обратите внимание, что в таблице женская аудитория имеет поле user_gender «female» или «f».](https://sql-academy.org/ru/trainer/tasks/99)

<details>
  <summary>Решение</summary>

```SQL
SELECT SUM(price * items) AS income_from_female
FROM Purchases
WHERE user_gender IN ('f', 'female')
```
</details>

56. [Удалить все перелеты, совершенные из Москвы (Moscow).](https://sql-academy.org/ru/trainer/tasks/56)

<details>
  <summary>Решение</summary>

```SQL
DELETE FROM trip
WHERE town_from = 'Moscow'
```
</details>


53. [Измените имя "Andie Quincey" на новое "Andie Anthony".](https://sql-academy.org/ru/trainer/tasks/53)

<details>
  <summary>Решение</summary>

```SQL
UPDATE FamilyMembers
SET member_name = 'Andie Anthony'
WHERE member_name = 'Andie Quincey'
```
</details>

74. [Выведите идентификатор и признак наличия интернета в помещении. Если интернет в сдаваемом жилье присутствует, то выведите «YES», иначе «NO».](https://sql-academy.org/ru/trainer/tasks/74)

<details>
  <summary>Решение</summary>

```SQL
SELECT id,
	if(has_internet = 1, "YES", "NO") as has_internet
FROM Rooms
```
</details>

75. [Выведите фамилию, имя и дату рождения студентов, кто был рожден в мае.](https://sql-academy.org/ru/trainer/tasks/75)

<details>
  <summary>Решение</summary>

```SQL
SELECT last_name,
	first_name,
	birthday
FROM Student
WHERE EXTRACT(
		MONTH
		from birthday
	) = 5
```
</details>




-- Online SQL Editor to Run SQL Online.
-- Use the editor to create new tables, insert data and all other SQL operations.

-- When working with SQL command words SELECT FROM should be uppercase while descriptives should be lower
-- TEXT = "hello" PRINT(TEXT)

-- SELECT used to get data, FROM specifying what table to get data from, * see everything from this
-- SELECT * FROM Customers;

-- SELECT * FROM Orders;

-- If I want to see first_name and last_name from customers what should I do?
-- SELECT first_name, last_name FROM Customers;

-- I want to see all customers from the UK 
-- SELECT * FROM Customers WHERE country == "UK";
-- SELECT * FROM Orders WHERE amount > 512;
-- SELECT * FROM Orders WHERE amount > 150 AND amount < 405;
-- SELECT * FROM Orders WHERE 405 < amount < 150; 
SELECT * FROM Customers ORDER BY last_name ASC;
SELECT * FROM Customers ORDER BY last_name DESC;

SELECT DISTINCT country FROM Customers ORDER BY country;

-- All Orders sorted by item and showing amount, order_id and item
SELECT amount, order_id, item FROM Orders ORDER BY item; 
-- All shippings where status is pending
SELECT * FROM Shippings WHERE status = "Pending";
-- All customers whose first name is john
SELECT * FROM Customers WHERE first_name = "John";
-- All orders where they ordered between 100 and 350
SELECT * FROM Orders WHERE amount BETWEEN 100 AND 350;
-- All customers ordered by country
SELECT * FROM Customers ORDER BY country;
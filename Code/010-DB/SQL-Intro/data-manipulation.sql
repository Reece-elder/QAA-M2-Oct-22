-- Data Manipulation Queries 
-- How can we edit / change the data: 

-- Create
-- INSERT INTO <table name> If you are not entering ALL values, you specify the columns you are adding
-- INSERT INTO Customers VALUES(6, 'Harry', 'Hill', 43, 'UK'); 
-- INSERT INTO Customers (customer_id, first_name, age) VALUES(7, 'Moby', 48); 

-- INSERT INTO Orders VALUES(6, 'Camera', 550, 6);

-- SQL - Standard Query Language, is a language for Relational Database Queries
-- MySQL AND pySQL use SQL, they are servers which use the language and have additional features and coding techniques 

-- Update - Updating certain records according to conditions in a table
-- SET is the new value
UPDATE Customers SET age = 999999 WHERE first_name = "John" AND last_name = "Doe";
UPDATE Shippings SET status = "Delivered";


-- Delete - Deleting our data, this can be dangerous 
DELETE FROM Customers WHERE first_name = "Moby";
DELETE FROM Customers WHERE customer_id = 6; -- Does work and is dangerous!
DELETE FROM Orders; -- Will delete everything within the table.. Don't do it
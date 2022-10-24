-- Creating tables to store data 
-- CREATE TABLE <table name> (column_name data_type, column_name data_type, PRIMARY KEY (column_name1)
-- int 123
-- float 12.20
-- char(10) abcde12345 (no more or less than 10 digits) IDs, SKU, Barcodes    
-- varchar(50) John Doe (no more than 50 chars, but can have less)
-- boolean 

-- CREATE TABLE movies (movie_id int NOT NULL UNIQUE, movie_name varchar(45) NOT NULL, runtime int NOT NULL, screen int NOT NULL, PRIMARY KEY (movie_id));

-- INSERT INTO movies (movie_name, runtime, screen) VALUES ("Toy Story 6", 78, 9);
--INSERT INTO movies VALUES (2, "Blade 7", 78, 4);  
-- INSERT INTO movies (movie_id) VALUES(12);

--CREATE TABLE ticket (ticket_id int NOT NULL UNIQUE, movie_id int NOT NULL, seat_num int NOT NULL, PRIMARY KEY (ticket_id) FOREIGN KEY (movie_id) REFERENCES movies(movie_id));

INSERT INTO ticket VALUES (1, 2, 18);

-- Delete our table
-- DROP TABLE movies;
 
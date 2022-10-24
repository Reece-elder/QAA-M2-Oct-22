# `pip --version` to check pip is installed 
# AS long as you have Python later than 2.5 you should have sqlite installed as default 

# Importing the sqlite package
import sqlite3

# Creating an object called conn, that is the connection to a new DB called "test-db"
conn = sqlite3.connect("test-db")

# Some way of communicating with the DB - cursor
cursor = conn.cursor()

createTableQuery = "CREATE TABLE birds(colour, flight, name)"
cursor.execute(createTableQuery) # Runs this command to create this table

# Gets all of the tables
query = "SELECT name FROM sqlite_master"

# whatever the query when executed gives us.. save as data
data = cursor.execute(query)

# Printing what the content of data is
print(data.fetchall())

# Exercise - Using sqlite create a database called "new-db" and create a table of your choice with 3+ fields and 1 primary key
# Using the "SELECT name FROM sqlite_master" print out the name of your table 
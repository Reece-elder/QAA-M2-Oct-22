from setup import createConn, createTable
from service import createRow, getAllData, getDataByID, deleteById

conn = createConn("prod-db")
cursor = conn.cursor()

# createTableString = "CREATE TABLE fruits (fruit_id int NOT NULL UNIQUE, colour varchar(30) NOT NULL, rating int NOT NULL, fruit_name varchar(30) NOT NULL, PRIMARY KEY (fruit_id));"
# createTable(cursor, createTableString)

#print(createRow(conn, "INSERT INTO fruits VALUES(1, 'blue', 8, 'Blueberries');"))
print(getAllData(conn, "fruits"))

def consoleInput():
    print(
        """
        Welcome to the DB!
        Please select an option, entering the number
        1. Create Data
        2. Get All Data
        3. Get One piece of Data
        4. Delete one piece of Data
        """
        )
    choice = input("Please enter an option: ")

    if choice == "1":
        createRowConsole()
    elif choice == "2":
        print(getAllData())
    elif choice == "3":
        getOneDataConsole()
    elif choice == "4":
        deleteOneConsole()

def createRowConsole():
    id = input("Please enter fruit id: ")
    colour = input("Please enter colour: ")
    rating = input("Please enter rating out of 10: ")
    name = input("Please enter name of fruit: ")
    query = f"INSERT INTO fruits VALUES({id}, '{colour}', {rating}, '{name}');"

    createRow(conn, query)

def getOneDataConsole():
    id = input("Please enter fruit id: ")
    print(getDataByID(conn, id))

def deleteOneConsole():
    id = input("Please enter fruit id: ")
    deleteById(conn, id)
    print(f"Fruit of {id} deleted")

consoleInput()

# fetch() isnt used but something like fetch to get data..
# apiData = fetch("api_url.com")

# Exercise - Using my code as reference, create your own basic CRD app 
# Creates a table, Create records, read all records, read one record(by id, name..), deletes one record

# Stretch goal(s):
# Use input to get inputs

# Add update queries
# Add a second table (relational) (TOUGH GOAL)
# Multiple files for resilience



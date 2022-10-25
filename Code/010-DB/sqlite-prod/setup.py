import sqlite3

def createConn(dbName):
    # Returning a connection object creating a DB of this name
    return sqlite3.connect(dbName)

# Make the table as part of setup, passing in 2 params
# Cursor to execute the command and the create table string
def createTable(cursor, query):
    cursor.execute(query) # Create our table
    return True 

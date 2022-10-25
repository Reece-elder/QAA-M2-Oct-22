# Takes in our connection object and a query to create data

def createRow(conn, query):
    conn.cursor().execute(query)
    conn.commit()
    return True

def getAllData(conn, tableName):
    data = conn.cursor().execute(f"SELECT * FROM {tableName}")
    listData = data.fetchall() # Converts from object to usable data
    return listData
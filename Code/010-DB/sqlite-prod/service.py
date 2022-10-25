# Takes in our connection object and a query to create data

# If we don't enter the correct ID, it will crash on us
# Try Catch Blocks, 
# Try: What we are 'Trying' to do
# Except / Catch: what to do if it fails
def createRow(conn, query):
    try:
        # Within the sqlite code, when there is an SQL error it has been coded to 
        # 'raise an exception' Create an exception object  
        conn.cursor().execute(query)
        conn.commit()
        return True
    except Exception as e:
        print(str(e))
        print("An Exception happened :(")
        # You can put in a try except block into an existing block
        # try: 
        #     number = 12
        # except:
    finally: 
        print("This will always run, regardless of whether there is exception or not")

def getAllData(conn, tableName):
    data = conn.cursor().execute(f"SELECT * FROM {tableName}")
    listData = data.fetchall() # Converts from object to usable data
    return listData

# Exception Handling
# Exception - Something that happens in the code that is not intended, and can potentially crash the app
# Exception handling is telling the code what to do, when it encounters an exception (I.e, wrong password on a site)


def getDataByID(conn, id):
    data = conn.cursor().execute(f"SELECT * FROM fruits WHERE fruit_id == {id}")
    listData = data.fetchall()
    return listData
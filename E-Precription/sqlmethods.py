import mysql.connector

mydb = mysql.connector.connect(
  host='sql6.freesqldatabase.com',
  user="sql6682428",
  password="x1uSP9bZTb",
  database='sql6682428'
)
def addUser():
    pass

def getUser():
    pass 
# WORK IS PENDINGGGGGGGGGG#sdasdasddasdasd
# need to create a function that takes values and inserts it to sql database using a query.
# then call it to register user route to store database of newly created user in sql database.
print(mydb)
cursorObject = mydb.cursor()
if __name__ =='__main__':
    ##cursorObject.execute("""CREATE TABLE USERS (
#                   Username  VARCHAR(200) NOT NULL,
#                   Email VARCHAR(50),
#                   phNumber INT,
#                   Password VARCHAR(200),
#                   IsDoc BOOL
#                   )""")
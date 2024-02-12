import mysql.connector

mydb = mysql.connector.connect(
  host='sql6.freesqldatabase.com',
  user="sql6682428",
  password="x1uSP9bZTb",
  database='sql6682428'
)
cursorObject = mydb.cursor()
def addUser(Username, Email,phNumber,Password,IsDoc):
    result =00
    data = (Username, Email,phNumber,Password,IsDoc)
    insert_stmt = ("INSERT INTO USERS(Username, Email, phNumber, Password, IsDoc) VALUES (%s, %s, %s, %s, %s)")
    try:
        cursorObject.execute(insert_stmt,data)
        mydb.commit()
        result=1
    except:
        result=0
    
    return result

def getUser(mail):
    select_stmt = "SELECT Username FROM USERS WHERE Email = %(emp_no)s"
    cursorObject.execute(select_stmt, { 'emp_no': mail })
    result = cursorObject.fetchall()
    return result
# to be called when user logs in. to show information on the user's homepage

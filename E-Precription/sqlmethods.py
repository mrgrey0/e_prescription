import mysql.connector

mydb = mysql.connector.connect(
  host='database-1.cj8208icggnk.eu-north-1.rds.amazonaws.com',
  user="admin",
  password="37Phw9prIcE6mRKEuwLM",
  database ='PRDATA'
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
    select_stmt = "SELECT * FROM USERS WHERE Email = %(mail)s"
    cursorObject.execute(select_stmt, { 'mail': mail })
    result = cursorObject.fetchall()
    return result
if __name__ =='__main__':
    r = getUser('test3@gmail.com')

    print(r) # returns the row of the table. use this to iterate the isDoc
    # to check isDoc use define a function to see the value of isDoc column of the selected row.


def findUser(mail):
    select_stmt = "SELECT Username FROM USERS WHERE Email = %(emp_no)s"
    cursorObject.execute(select_stmt)
# to be called when user logs in. to show information on the user's homepage

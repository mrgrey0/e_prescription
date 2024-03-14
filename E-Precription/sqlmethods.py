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

def getMedicineData(name):
    #cursorObject.execute("SELECT * FROM presMeds WHERE patientName = '{patient_name}'")
    #return cursorObject.fetchall()

    select_stmt = "SELECT * FROM presMeds WHERE patientName = %(name)s"
    cursorObject.execute(select_stmt, { 'name': name })
    result = cursorObject.fetchall()
    return result

def addMedication(name,data):
    try:
        # Prepare SQL query using parameterized placeholders for security
        sql = """
            INSERT INTO presMeds (patientName, symptoms, medicine, duration, quantity, dosage)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

            # Iterate through medicine_data and execute the query for each medicine
        for medicine in data:
            cursorObject.execute(sql, (name,medicine['symptom'], medicine["medicine"], medicine["duration"], medicine["quantity"], medicine["feeding_rule"]))
            mydb.commit()
            print("Medicine data inserted successfully!")
    except mysql.connector.Error as err:
        print("Error inserting data:", err)

def addPatientToDb(patientName, patientAge, patientGender, patientWeight, patientPhone):
    result =00
    data = (patientName, patientAge, patientGender, patientWeight, patientPhone)
    insert_stmt = ("INSERT INTO PATIENTS(patientName, patientAge, patientGender, patientWeight, patientPhone) VALUES (%s, %s, %s, %s, %s)")
    try:
        cursorObject.execute(insert_stmt,data)
        mydb.commit()
        result=1
    except:
        result=0
    
    return result

def getAllPatients():
    query ="SELECT patientName, patientAge, patientGender, patientWeight, patientPhone FROM PATIENTS;"
    cursorObject.execute(query)
    patients = cursorObject.fetchall()
    return patients

def getMedicineDetails():
    query = "SELECT symptoms, Medicines, Dosage FROM your_table"
    cursorObject.execute(query)
    data = cursorObject.fetchall()
    return data
#if __name__ =='__main__':
#    r = getAllPatients()
#    print(r)

#    print(r) # returns the row of the table. use this to iterate the isDoc
    # to check isDoc use define a function to see the value of isDoc column of the selected row.


def findUser(mail):
    select_stmt = "SELECT Username FROM USERS WHERE Email = %(emp_no)s"
    cursorObject.execute(select_stmt)
# to be called when user logs in. to show information on the user's homepage
# to be continued after the whole work is completed

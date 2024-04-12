import pyrebase
import sqlmethods
firebaseConfig = {
  'apiKey': "AIzaSyDqoRHH1cbTWLUYRlH1vP5R-zrkCCAT0MI",
  'authDomain': "e-prescription-ff041.firebaseapp.com",
  'projectId': "e-prescription-ff041",
  'storageBucket': "e-prescription-ff041.appspot.com",
  'messagingSenderId': "437020753136",
  'appId': "1:437020753136:web:c2c432dd239a9debfe1635",
  'databaseURL': ''
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def login(email,password):
    res = sqlmethods.getUser(email)
    if not res :
         return 0 # tell the user dont exit
    else : # log in the user
        result = ''
        try:
            login = auth.sign_in_with_email_and_password(email,password)
            result = 'success'
        except :
            result = 'unsuccess'
        return result

def signUp(mail,passW,uName,phNo,isDoc):
        result = ''
        try:
            login = auth.create_user_with_email_and_password(mail,passW)
            res = sqlmethods.addUser(uName,mail,phNo,passW,isDoc)
            result ='success'
        except :
            result = 'unsuccess'
        return result
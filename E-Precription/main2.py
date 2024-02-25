from flask import Flask, flash, redirect, render_template,request, url_for
import auth_methods
import sqlmethods

app = Flask(__name__)
app.secret_key = "diu290u32fh048y224r24r24rfd"

pName =''
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def loginPg():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template("welcome.html")

@app.route('/homerecep')
def homerecep():
    r= sqlmethods.getAllPatients()
    return render_template("reception.html",patients=r)

@app.route('/homedoc')
def homedoc():
    r= sqlmethods.getAllPatients()
    return render_template("doctor.html",patients=r)

@app.route('/view/<name>')
def view(name):
    pass
     # view the patient data from doctor's side
# this will be used to view the patient or to send request to sql server to view the patient information.

@app.route('/addPatient',methods=['GET','POST'])
def addPatient():
    if request.method =='POST':
        patientName=request.form['name']
        patientAge=request.form['age']
        patientGender=request.form['gender']
        patientWeight=request.form['weight']
        patientPhone = request.form['phone']

        r = sqlmethods.addPatientToDb(patientName,patientAge,patientGender,patientWeight,patientPhone)
        if r == 1:
            flash('Data saved successfully!', 'success')
        else:
            flash('There was some error while saving the data, please try again.')

        return redirect(url_for('homerecep'))

@app.route('/contact')
def contact():
    return render_template("c3.html")

@app.route('/regusr',methods =['GET','POST'])
def regusr():
    if request.method =='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        phNumber=request.form['phNumber']
        isDoc = request.form['check_box'] == 'doctor'

        res = auth_methods.signUp(email,password,username,phNumber,isDoc)
        if res =='success':
            return redirect(url_for('homepage'))
            
        elif res =='unsuccess':
            return "SOMETHING WENT WRONG"

@app.route('/loginChck',methods=['POST','GET'])
def checklogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        res = auth_methods.login(username,password)
        if res=='success':
            # add sql method to chek if the account is doctor or not.
            return redirect(url_for('homepage'))
        elif res == 'unsuccess':
            return "<P>Something went wrong</P>"
    else :
        return "NONE"
    


@app.route('/prescribe/<name>',methods=['GET','POST'])
def pres(name):
    pName = name
    if request.method=='GET':
        return render_template('prescribe.html',patientName=name)
    elif request.method=='POST':
        medicine_data = []
        for row in range(len(request.form.getlist('medicineName'))):
            medicine_data.append({
            "medicine": request.form.getlist('medicineName')[row],
            "duration": request.form.getlist('duration')[row],
            "quantity": request.form.getlist('quantity')[row],
            "feeding_rule": request.form.getlist('feedingRules')[row]
            })
# add a method to store the databse of medicines to databbase and also print it 
            sqlmethods.addMedication(pName,medicine_data)
    return "DONE"

if __name__ == '__main__':
    app.run(debug=True)
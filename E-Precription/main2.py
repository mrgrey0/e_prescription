from flask import Flask, flash, redirect, render_template,request, url_for, make_response
import auth_methods
import sqlmethods
#from pdf_code import generate
from fpdf import FPDF
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField

class MedicationForm(FlaskForm):
    symptoms = SelectField('Symptoms',choices=['Fever','Hedache','WBC Drop','Body Pain','Rashes','Platelets Drop','High Fever','Body Pain','Hedache','Abdomen Pain','WBC Increase','Cough/Sneezing','Fever','Hedache','Body Pain','Watery/Red eyes','WBC Decrease','Lose Motion','Migration','Weakness','Dehidration','Fever','Abdomen Pain','Vomiting','Headache','Fast Heart Rate','Chest Pain','Cough/Cough with Blood','Night Sweats','Weight Loss',])  # Optional field
    medicine_name = SelectField('Medicine Name', choices=['Inj. Pan 40mg','Betadine Gargle','Cap. Fluvir 75mg','Cap. Vibact','Cap. Vibact ','Inj. Amikacin 500','Inj. Amikacin 500gm','Inj. Amkacin 500','Inj. Artisam 120gm','Inj. Artisunate 120gm','Inj. Finecef 1gm','Inj. Finecef T 1.125gm','Inj. Maxotan 4.5','Inj. Merosure 1gm','Inj. Pan 40mg','Inj. Pantop 40gm','Inj. Pipzo 4.5','Inj. Swich XP 1.125gm','Inj. Zostum 1.5gm','IU DNS RL','IU RL NS','Nab. Duolin Budecort','Syp. Ascoril Ls','Syp. Brozety','Syp. Grilli','Tab. Dolo 650','Tab. Lomotile(Sos)','Tab. Xycass 650(sos)','Tb. Akurit 400(6 months)','Tb. B. Complex','Tb. Caripap','Tb. Clabum 626','Tb. Doxy 100.','Tb. Drotin M.','Tb. Mucinac 600mg','Tb. Nicip Plus','Tb. Nicip Plus','Tb. Pan 40mg','Tb. Sumoflam','Tb. Xycaa 650','Tb. Xycaa 650(Sos)'] )  # Optional field
    duration = IntegerField('Duration (days)' )  # Optional field
    quantity = IntegerField('Quantity')  # Optional field
    feeding_rules = SelectField('Dosage', choices=['Once a day','Twice a day','Thrice a day'])

def generate(patient_name, data):
  """
  Generates a prescription PDF for the given patient and data.

  Args:
      patient_name: Name of the patient.
      data: List of tuples containing prescription details.

  Returns:
      A byte string containing the PDF data.
  """
  pdf = FPDF()
  pdf.add_page()

  # Hospital and Doctor Information (Edit as needed)
  pdf.set_font("Arial", size=12)
  pdf.cell(200, 10, txt="Sai Hospital - Dr. Rajendra Dilip Pardeshi B.A.M.S CCH, MD(sch) GENERAL PHYSICIAN", ln=1, align='C')
  pdf.cell(200, 10, txt="Address: Indranil Corner, Yeola Contact: 9421212322", ln=2, align='C')

  # Patient Name
  pdf.cell(200, 10, txt=patient_name, ln=2, align='L')

  # Prescription Details Header
  pdf.set_font("Arial", size=10)
  pdf.cell(60, 10, txt="Symptoms", border=1, align='C')
  pdf.cell(60, 10, txt="Medicine", border=1, align='C')
  pdf.cell(40, 10, txt="Duration", border=1, align='C')
  pdf.cell(40, 10, txt="Quantity", border=1, align='C')
  pdf.cell(40, 10, txt="Dosage", border=1, ln=1, align='C')

  # Populate prescription details
  for row in data:
      #symptoms, medName, duration, quantity, dosage = row
      pdf.set_font("Arial", size=10)
      pdf.cell(60, 10, txt=row[1], border=1, align='L')
      pdf.cell(60, 10, txt=row[2], border=1, align='L')
      pdf.cell(40, 10, txt=str(row[3]), border=1, align='C')
      pdf.cell(40, 10, txt=str(row[4]), border=1, align='C')
      pdf.cell(40, 10, txt=row[5], border=1, ln=1, align='L')

  filename = f"prescription_{patient_name}.pdf"  # Generate filename directly
  pdf.output(filename, 'F')  # Save PDF with generated filename
  return filename  


app = Flask(__name__)
app.secret_key = "diu290u32fh048y224r24r24rfd"

pName =''
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def homepg():
    return render_template('home22.html')

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
    form = MedicationForm()
    pName = name
    if request.method=='GET':
        #s = sqlmethods.getSymptoms()
        #m = sqlmethods.getMedicine()
        #print(s)
        return render_template('prescribe.html',patientName=name,form=form)
    elif request.method=='POST':
        form = MedicationForm()
        if form.validate_on_submit():  # Validate the form data
            symptoms = []
            medicine_names = []
            durations = []
            quantities = []
            dosages = []

            # Loop through each form object (one per row)
            for key, value in request.form.items():
                if key.startswith('symptoms_'):
                    symptoms.append(value)
                elif key.startswith('medicine_name_'):
                    medicine_names.append(value)
                elif key.startswith('duration_'):
                    durations.append(int(value))  # Convert duration to integer
                elif key.startswith('quantity_'):
                    quantities.append(int(value))  # Convert quantity to integer
                elif key.startswith('dosage_'):
                    dosages.append(value)

            # Call your medication adding function with the list of medication data
            print(pName)
            print(symptoms,medicine_names,durations,quantities,dosages)
            #sqlmethods.addMedication(pName, medicine_data)

#        medicine_data = []
#        for row in request.form:
#            medicine_data.append({
#            "symptom" : request.form.get('symptomsl'),
#            "medicine": request.form.get('medicineName'),
#            "duration": request.form.get('duration'),
#            "quantity": request.form.get('quantity'),
#            "feeding_rule": request.form.get('feedingRules')
#            })
            
            #sqlmethods.addMedication(pName,medicine_data)

            prescription_data = sqlmethods.getMedicineData(pName)
            #print(prescription_data)
            filename = generate(pName, prescription_data)
            response = make_response(filename, 200)
            response.headers['Content-Type'] = 'application/pdf'
            response.headers['Content-Disposition'] = f'attachment; filename={filename}'
        return "SUCESS"

if __name__ == '__main__':
    app.run(debug=True)
import io

from flask import Flask, flash, redirect, render_template, request, url_for, make_response
# from pdf_code import generate
from fpdf import FPDF

import auth_methods
import sqlmethods


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
    pdf.cell(200, 10, txt="Sai Hospital - Dr. Rajendra Dilip Pardeshi B.A.M.S CCH, MD(sch) GENERAL PHYSICIAN", ln=1,
             align='C')
    pdf.cell(200, 10, txt="Address: Indranil Corner, Yeola Contact: 9421212322", ln=2, align='C')

    # Patient Name
    pdf.cell(200, 10, txt="Name : " + patient_name, ln=2, align='L')

    # Prescription Details Header
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, txt="Symptoms", border=1, align='C')
    pdf.cell(40, 10, txt="Medicine", border=1, align='C')
    pdf.cell(20, 10, txt="Duration", border=1, align='C')
    pdf.cell(20, 10, txt="Quantity", border=1, align='C')
    pdf.cell(40, 10, txt="Dosage", border=1, ln=1, align='C')

    # Populate prescription details
    for row in data:
        # symptoms, medName, duration, quantity, dosage = row
        pdf.set_font("Arial", size=10)
        pdf.cell(40, 10, txt=row[1], border=1, align='L')
        pdf.cell(40, 10, txt=row[2], border=1, align='L')
        pdf.cell(20, 10, txt=str(row[3]), border=1, align='C')
        pdf.cell(20, 10, txt=str(row[4]), border=1, align='C')
        pdf.cell(40, 10, txt=row[5], border=1, ln=1, align='L')

    # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    #     pdf.output(temp_file.name, 'F')
    #     pdf_url = temp_file.name
    # return pdf_url

    pdf_data = io.BytesIO()
    pdf.output(pdf_data, 'F')
    pdf_data.seek(0)

    response = make_response(pdf_data.getvalue())

    # Set response headers
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=prescription_{patient_name}.pdf'

    return response
    # return pdf_data.getValue()


app = Flask(__name__)
app.secret_key = "diu290u32fh048y224r24r24rfd"

pName = ''


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def loginPg():
    return render_template('login.html')


@app.route("/")
def index():
    return render_template("welcome.html")


@app.route('/homerecep')
def homerecep():
    r = sqlmethods.getAllPatients()
    return render_template("reception.html", patients=r)


@app.route('/homedoc')
def homedoc():
    r = sqlmethods.getAllPatients()
    return render_template("doctor.html", patients=r)


@app.route('/view/<name>')
def view(name):
    pass
    # view the patient data from doctor's side


# this will be used to view the patient or to send request to sql server to view the patient information.

@app.route('/addPatient', methods=['GET', 'POST'])
def addPatient():
    if request.method == 'POST':
        patientName = request.form['name']
        patientAge = request.form['age']
        patientGender = request.form['gender']
        patientWeight = request.form['weight']
        patientPhone = request.form['phone']

        r = sqlmethods.addPatientToDb(patientName, patientAge, patientGender, patientWeight, patientPhone)
        if r == 1:
            flash('Data saved successfully!', 'success')
        else:
            flash('There was some error while saving the data, please try again.')

        return redirect(url_for('homerecep'))


@app.route('/contact')
def contact():
    return render_template("c3.html")


@app.route('/regusr', methods=['GET', 'POST'])
def regusr():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phNumber = request.form['phNumber']
        isDoc = request.form['check_box'] == 'doctor'

        res = auth_methods.signUp(email, password, username, phNumber, isDoc)
        if res == 'success':
            return redirect(url_for('homepage'))

        elif res == 'unsuccess':
            return "SOMETHING WENT WRONG"


@app.route('/loginChck', methods=['POST', 'GET'])
def checklogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        res = auth_methods.login(username, password)
        if res == 'success':
            # add sql method to chek if the account is doctor or not.
            doc = sqlmethods.isDoc(username)
            if doc == "YES":
                return redirect(url_for('homedoc'))
            elif doc == "NO":
                return redirect(url_for('homerecep'))
        elif res == 'unsuccess':
            return "<P>Something went wrong</P>"
        elif res == 0:
            return "MMMMM"
    else:
        return "NONE"


@app.route('/prescribe/<name>', methods=['GET', 'POST'])
def pres(name):
    pName = name
    if request.method == 'GET':
        return render_template('press2.html', patientName=name)
    elif request.method == 'POST':
        # form = MedicationForm()
        # if form.validate_on_submit():  # Validate the form data
        # Access form data
        symptoms_list = request.form.getlist('symptoms[]')  # List of symptoms for each row
        medicine_names_list = request.form.getlist('medicine_name[]')  # List of medicine names for each row
        durations_list = request.form.getlist('duration[]')  # List of durations for each row
        quantities_list = request.form.getlist('quantity[]')  # List of quantities for each row
        feeding_rules_list = request.form.getlist('feeding_rules[]')  # List of feeding rules for each row

        # Loop through each row and access data
        for i in range(len(symptoms_list)):
            symptoms = symptoms_list[i]
            medicine_name = medicine_names_list[i]
            duration = durations_list[i]
            quantity = quantities_list[i]
            feeding_rule = feeding_rules_list[i]

            print(
                f"Patient: {pName}, Symptoms: {symptoms}, Medicine: {medicine_name}, Duration: {duration} days, Quantity: {quantity}, Feeding Rule: {feeding_rule}")
            # Process data for each row (e.g., print, insert into database)

        sqlmethods.addMedication(pName, symptoms_list, medicine_names_list, durations_list, quantities_list,
                                 feeding_rules_list)

        prescription_data = sqlmethods.getMedicineData(pName)

        data = generate(pName, prescription_data)
        # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        #    temp_file.write(filename)
        #    file_path = temp_file.name  # Get the temporary file path

        #response = make_response(pdf_data)
        #response.headers['Content-Type'] = 'application/pdf'
        #response.headers['Content-Disposition'] = 'attachment; filename=prescription_{}.pdf'.format(pName)
        #return response


@app.route('/view_prescription', methods=['GET', 'POST'])
def view_prescription():
    return render_template('render_pdf.html')


if __name__ == '__main__':
    app.run(debug=True)

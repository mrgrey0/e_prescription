from fpdf import FPDF

def getMedicineData(patient_name, data):
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
  pdf.cell(200, 10, txt=f"Patient Name: {patient_name}", ln=2, align='L')

  # Prescription Details Header
  pdf.set_font("Arial", size=10)
  pdf.cell(60, 10, txt="Symptoms", border=1, align='C')
  pdf.cell(60, 10, txt="Medicine", border=1, align='C')
  pdf.cell(40, 10, txt="Duration", border=1, align='C')
  pdf.cell(40, 10, txt="Quantity", border=1, align='C')
  pdf.cell(40, 10, txt="Dosage", border=1, ln=1, align='C')

  # Populate prescription details
  for row in data:
      symptoms, medName, duration, quantity, dosage = row
      pdf.set_font("Arial", size=10)
      pdf.cell(60, 10, txt=symptoms, border=1, align='L')
      pdf.cell(60, 10, txt=medName, border=1, align='L')
      pdf.cell(40, 10, txt=str(duration), border=1, align='C')
      pdf.cell(40, 10, txt=str(quantity), border=1, align='C')
      pdf.cell(40, 10, txt=dosage, border=1, ln=1, align='L')

  pdf.output(f"prescription_{patient_name}.pdf", 'F')
  return f"prescription_{patient_name}.pdf"

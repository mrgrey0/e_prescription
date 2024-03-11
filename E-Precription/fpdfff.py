from fpdf import FPDF

# Create a new FPDF instance
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font
pdf.set_font(family='Arial', size=10)

# Create the hospital name header
pdf.cell(0, 10, txt='SAI HOSPITAL', ln=1, align='C')

# Create the doctor information section
pdf.cell(100, 5, txt='Dr. Rajendra Dilip Pardeshi', ln=0)
pdf.cell(0, 5, txt='B.A.M.SCCH, MD(sch) GENRAL PHSICIAN', ln=1)
pdf.cell(100, 5, txt='Address: Indranil Corner, Yoola', ln=0)
pdf.cell(0, 5, txt='Contact: 9421212322', ln=1)

# Add a space
pdf.cell(0, 5, txt='', ln=1)

# Create labels for patient information
pdf.cell(30, 5, txt='Patient Name:')
pdf.cell(40, 5, txt='')  # Placeholder for name
pdf.cell(20, 5, txt='Date:')
pdf.cell(0, 5, txt='')  # Placeholder for date
pdf.ln(5)

pdf.cell(30, 5, txt='Age:')
pdf.cell(20, 5, txt='')  # Placeholder for age
pdf.cell(15, 5, txt='Gender:')
pdf.cell(20, 5, txt='')  # Placeholder for gender
pdf.cell(20, 5, txt='Weight:')
pdf.cell(0, 5, txt='')  # Placeholder for weight
pdf.ln(5)

pdf.cell(30, 5, txt='Address:')
pdf.cell(0, 5, txt='')  # Placeholder for address
pdf.ln(5)

pdf.cell(30, 5, txt='Contact:')
pdf.cell(0, 5, txt='')  # Placeholder for contact

# Add a space
pdf.ln(10)

# Create title for medicines section
pdf.cell(0, 5, txt='Medicines:', ln=1)

# Create columns for disease, dosage, and duration
pdf.cell(60, 5, txt='Disease & Symptoms', border=1)
pdf.cell(60, 5, txt='Dosage & Duration', border=1)
pdf.ln(5)

# Add rows for medicines (you can add more rows as needed)
pdf.cell(60, 5, txt='', border=1)
pdf.cell(60, 5, txt='', border=1)
pdf.ln(5)
pdf.cell(60, 5, txt='', border=1)
pdf.cell(60, 5, txt='', border=1)
pdf.ln(5)

# Add a space
pdf.ln(10)

# Titles for tests and follow-up sections
pdf.cell(30, 5, txt='Tests Recommanded:')
pdf.cell(0, 5, txt='Follow up:')
pdf.ln(5)

# Text boxes for tests and follow-up
pdf.cell(0, 20, txt='', border=1, ln=1)
pdf.cell(60, 5, txt='Sign:', border=1)
pdf.cell(0, 5, txt='', border=1)

# Save the PDF
pdf.output("prescription_form.pdf")

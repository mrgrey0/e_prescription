from fpdf import FPDF

# Database connection and data retrieval (Modify for your database)
patient_name = "John Doe"  # Replace with retrieved name
date = "2024-03-11"  # Replace with retrieved date
# ... other patient data retrieval

# Fetch medicine categories from database (replace with your code)
medicine_categories = ["Antibiotics", "Pain Medication", "Other"]

# Create a new FPDF instance and set default font
pdf = FPDF()
pdf.set_font(family='Arial', size=10)

# Define colors (replace with desired RGB values)
hospital_name_color = (0, 0, 128)  # Dark blue
doctor_info_color = (0, 128, 0)  # Green
title_color = (64, 0, 64)  # Dark purple
text_color = (0, 0, 0)  # Black

# Add a page
pdf.add_page()

# Create the hospital name header with color
pdf.set_text_color(*hospital_name_color)  # Set text color for hospital name
pdf.cell(0, 10, txt='SAI HOSPITAL', ln=1, align='C')

# Create the doctor information section with color
pdf.set_text_color(*doctor_info_color)  # Set text color for doctor info
pdf.cell(100, 5, txt='Dr. Rajendra Dilip Pardeshi', ln=0)
pdf.cell(0, 5, txt='B.A.M.SCCH, MD(sch) GENERAL PHSICIAN', ln=1)
pdf.cell(100, 5, txt='Address: Indranil Corner, Yoola', ln=0)
pdf.cell(0, 5, txt='Contact: 9421212322', ln=1)

# Add a space
pdf.cell(0, 5, txt='', ln=1)

# Set text color back to black for labels
pdf.set_text_color(*text_color)  # Reset text color

# Create labels for patient information
pdf.cell(30, 5, txt='Patient Name:')
pdf.cell(40, 5, txt=patient_name)
pdf.cell(20, 5, txt='Date:')
pdf.cell(0, 5, txt=date)
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

# Create title for medicines section with color
pdf.set_text_color(*title_color)  # Set text color for title
pdf.cell(0, 5, txt='Medicines:', ln=1)

# Create columns for disease, dosage, and duration
pdf.set_text_color(*text_color)  # Reset text color
pdf.cell(60, 5, txt='Disease & Symptoms', border=1)
pdf.cell(60, 5, txt='Dosage & Duration', border=1)
pdf.ln(5)

# Loop for medicine categories with placeholders
for medicine_category in medicine_categories:
    pdf.cell(60, 5, txt=medicine_category, border=1)
    pdf.cell(60, 5, txt="Dosage to be determined by physician", border=1)
    pdf.ln(5)

# Add a space
pdf.ln(10)

# Titles for tests and follow-up sections with color
pdf.set_text_color(*title_color)  # Set text color

# Save the PDF
pdf.output("prescription_form.pdf")

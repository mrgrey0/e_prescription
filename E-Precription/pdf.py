from reportlab.pdfgen import canvas

PAGE_WIDTH = 595  # Width in points (1 point = 1/72 inch)
PAGE_HEIGHT = 842  # Height in points (standard A4 paper size)
LEFT_MARGIN = 50  # Adjust margins as needed

def generate_pdf(data):
  
   pdf = canvas.Canvas("output.pdf", pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
   pdf.translate(LEFT_MARGIN, PAGE_HEIGHT)
  
   font_size = 10
   font_name = "Helvetica"

   y_pos = PAGE_HEIGHT - 50  # Start from top and move down

   pdf.setFont(font_name, font_size + 4)
   pdf.drawString(LEFT_MARGIN, y_pos, "Your Report Title")
   y_pos -= 20
   for row in data:
        pdf.setFont(font_name, font_size)
        pdf.drawString(LEFT_MARGIN, y_pos, f"Symptoms: {row[0]}")
        pdf.drawString(LEFT_MARGIN, y_pos - 15, f"Medicines: {row[1]}")
        pdf.drawString(LEFT_MARGIN, y_pos - 30, f"Dosage: {row[2]}")
        y_pos -= 40  # Adjust spacing between data points
   pdf.save()

def gen2():
    pdf = canvas.Canvas("output.pdf", pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    pdf.translate(LEFT_MARGIN, PAGE_HEIGHT)
  
    font_size = 10
    font_name = "Helvetica"

    y_pos = PAGE_HEIGHT - 50  # Start from top and move down

    pdf.setFont(font_name, font_size + 4)
    pdf.drawString(LEFT_MARGIN, y_pos, "Your Report Title")
    y_pos -= 40  # Adjust spacing between data points
    pdf.drawString(LEFT_MARGIN, y_pos, "Ssadadfsdfdfsdasdmptoms:")
    pdf.save()

if __name__ == '__main__':
    gen2()
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger, PdfFileReader
import os

# Define the headlines, text, and image you want to include in the PDF
headlines = ["Python projekt"]
text = ["""hehe"""]
image_path = "graf.png"

# Set up the ReportLab canvas and stylesheet
canvas = canvas.Canvas("Python_projekt.pdf", pagesize=letter)
styles = getSampleStyleSheet()
style = styles['Normal']

# Define the x and y coordinates for the headlines, text, and image
x_coord = 1.5 * inch
y_coord = 10 * inch

# Add the headlines and text to the canvas
for headline, text in zip(headlines, text):
    canvas.setFont("Helvetica-Bold", 16)
    canvas.drawString(x_coord, y_coord, headline)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(x_coord, y_coord - 0.5 * inch, text)
    y_coord -= 1 * inch

# Add the image to the canvas
canvas.drawImage(image_path, x_coord, y_coord - 3 * inch, width=3*inch, height=3*inch)

# Save the canvas to a PDF file
canvas.save()

# Merge the generated PDF with an existing PDF (optional)
existing_pdf = PdfFileReader(open("existing.pdf", "rb"))
output_pdf = PdfFileReader(open("Python_projekt.pdf", "rb"))
merger = PdfFileMerger()
merger.append(existing_pdf)
merger.append(output_pdf)
merger.write("merged.pdf")

# Remove the temporary output file
os.remove("Python_projekt.pdf")
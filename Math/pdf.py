from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger, PdfFileReader
import os

# Define the headlines and text you want to include in the PDF
headlines = ["Headline 1", "Headline 2", "Headline 3"]
text = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 
        "Vivamus consectetur neque vel lectus tristique malesuada.", 
        "Duis vitae elit vel sapien pretium tincidunt."]

# Set up the ReportLab canvas and stylesheet
canvas = canvas.Canvas("output.pdf", pagesize=letter)
styles = getSampleStyleSheet()
style = styles['Normal']

# Define the x and y coordinates for the headlines and text
x_coord = 1.5 * inch
y_coord = 10 * inch

# Add the headlines and text to the canvas
for headline, text in zip(headlines, text):
    canvas.setFont("Helvetica-Bold", 16)
    canvas.drawString(x_coord, y_coord, headline)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(x_coord, y_coord - 0.5 * inch, text)
    y_coord -= 1 * inch

# Save the canvas to a PDF file
canvas.save()

# Merge the generated PDF with an existing PDF (optional)
existing_pdf = PdfFileReader(open("existing.pdf", "rb"))
output_pdf = PdfFileReader(open("output.pdf", "rb"))
merger = PdfFileMerger()
merger.append(existing_pdf)
merger.append(output_pdf)
merger.write("merged.pdf")

# Remove the temporary output file
os.remove("output.pdf")
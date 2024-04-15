from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch 
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter, A4
import psycopg2
import main
from main import name_entry, name

'''width = 80
height = 210
pdf='D:\\Krishna sai\\Ktinker\\receipt.pdf'''

def generate_pdf():
    width = 80
    height = 210
    pdf='D:\\Krishna sai\\Ktinker\\receipt.pdf'

    c=canvas.Canvas(pdf,pagesize=(width,height))
    c.setStrokeColor('Black')
    c.rect(0.1*inch,0.1*inch,0.9*inch,2.7*inch,fill=0)
    c.setFillColor('Black')
    c.setFont("Helvetica", 4)
    c.drawRightString(0.8*inch, 2.7*inch, 'hi')

    c.showPage()
    c.save()
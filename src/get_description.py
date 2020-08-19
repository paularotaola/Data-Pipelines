import requests
import json
from parse import parser 
from fpdf import FPDF


def get_description(x):
    try:      
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{x}"
        res = requests.get(url).json()
        title = res["items"][0]["volumeInfo"]["title"]
        author = res["items"][0]["volumeInfo"]["authors"][0]
        description = res["items"][0]["volumeInfo"]["description"]
        pages = res["items"][0]["volumeInfo"]["pageCount"]
        sales = res["items"][0]["saleInfo"]["isEbook"]

        title2 = "Your Book Report"
        pdf = FPDF('P','mm','A4')
        pdf.add_page()
        pdf.set_font('Courier', 'B', 20)
        pdf.cell(180, 20, txt="Your Book Report!", ln=1, align="C")
        pdf.ln(5)
        pdf.set_font('Courier', 'B', 14)
        pdf.cell(180, 10, txt="Title:", ln=1, align="L")
        pdf.set_font('Courier', '', 12)
        pdf.multi_cell(180,8,f"{title}",0,1,'C')
        pdf.set_font('Courier', 'B', 14)
        pdf.cell(180, 10, txt="Author:", ln=1, align="L")
        pdf.set_font('Courier', '', 12)
        pdf.multi_cell(180,8,f"{author}",0,1,'C')
        pdf.ln(5)
        pdf.set_font('Courier', 'B', 14)
        pdf.cell(180, 10, txt="Description", ln=1, align="L")
        pdf.set_font('Courier', '', 12)
        pdf.multi_cell(190,8,f"{description}",0,2,'C')
        pdf.image('Input/books.jpg', x=50, y=230, w=80)
        
        return f"Your Book Recommedation ==>", {
        "==> Title": title, 
        "==> Author": author, 
        "==> Description": description, 
        "==> Number of pages": pages}, pdf.output("Output/book-report.pdf")
    
    except KeyError:
        return "Sorry, no book recommendation available in Google Books :("
    
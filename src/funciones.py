import requests
import json
import pandas as pd
from fpdf import FPDF
from parse import parser 


result = pd.read_csv("Output/books_output.csv")
result = pd.DataFrame(result)

"""def genres(genre):
    if genre == "novel":
        return 335
    elif genre == "poetry":
        return 284
    elif genre == "drama":
        return 2512
    elif genre == "adventure":
        return 342
    elif genre == "romance":
        return 358  
    elif genre == "thriller":
        return 339
    elif genre == "biographies":
        return 131
    elif genre == "comic":
        return 98
    elif genre == "science fiction":
        return 2626
    elif genre == "science ":
        return 2534
    elif genre == "kids ":
        return 2491
    elif genre == "mental-health ":
        return 1300"""
   

def output(x,y):
    x = float(x)
    n = result[(result["year"]== x) & (result["categories"].str.contains(f"{y}"))& (result["rating-avg"]>1)].sort_values(by="rating-avg",ascending=False).head(1)
    return n


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
        pdf.image('books.jpg', x=50, y=230, w=80)

        return f"Your Book Recommedation ==>", f"Title: {title}", f"==>Author: {author}", f"==>Description: {description}", f" ==>Number of pages: {pages}",f"Available in ebook?: {sales}", pdf.output("book-report.pdf")
    
    except KeyError:
        return  "No book recommendation for this year :("
    


  
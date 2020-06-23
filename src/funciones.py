import requests
import json
import pandas as pd
from fpdf import FPDF
from parse import parser 


result = pd.read_csv("Output/books_output.csv")
result = pd.DataFrame(result)

def genres(y):
    """
    Filters the genre with the corresponding category in the dataset
    """
    if y == "novel":
        y =335
        return y
    elif y == "poetry":
        y = 284
    elif y == "drama":
        y =2512
    elif y == "adventure":
        y =342
    elif y == "romance":
        y =358  
    elif y == "thriller":
        y =339
    elif y == "biographies":
        y =131
    elif y == "comic":
        y= 98
    elif y == "science fiction":
        y= 2626
    elif y == "science":
        y =2534
    elif y == "kids":
        y =2491
    elif y == "mental-health":
        y =1300
    return y

def output(x,y):
    """
    Filters the dataset with the year and genre
    """
    x = float(x)
    if y == "novel":
        y =2466
    elif y == "poetry":
        y = 284
    elif y == "drama":
        y =2512
    elif y == "adventure":
        y =342
    elif y == "romance":
        y =358  
    elif y == "thriller":
        y =339
    elif y == "biographies":
        y =131
    elif y == "comic":
        y= 2979
    elif y == "science-fiction":
        y= 2626
    elif y == "science":
        y =2534
    elif y == "kids":
        y =2491
    elif y == "horror":
        y =2624
    elif y == "mental-health":
        y =1300

    filtered = result[(result["year"]== x) & (result["categories"].str.contains(f"{y}"))& (result["rating-avg"]>1)].sort_values(by="rating-avg",ascending=False).head(1)
    return filtered


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

        return f"Your Book Recommedation ==>", f"Title: {title}", f"==>Author: {author}", f"==>Description: {description}", f" ==>Number of pages: {pages}",f"Available in ebook?: {sales}", pdf.output("book-report.pdf")
    
    except KeyError:
        return "Sorry, no book recommendation available in Google Books :("
    


  
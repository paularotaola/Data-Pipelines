import pandas as pd
import requests
from IPython.display import Image

result = pd.read_csv("Output/books_output.csv")
result = pd.DataFrame(result)
result.head(5).sort_values(by="year", ascending=False)


def output(x,y):
    return result[(result["year"]== x) & (result["categories"].str.contains(f"{y}"))& (result["rating-avg"]>3.5)].sort_values(by="rating-avg",ascending=False).head(1)

n = output(2019.0, 10)
x = pd.unique(n["isbn10"]).tolist()

def get_description(x):

    try:      
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{x}"
        res = requests.get(url).json()
        title = res["items"][0]["volumeInfo"]["title"]
        author = res["items"][0]["volumeInfo"]["authors"][0]
        description = res["items"][0]["volumeInfo"]["description"]
        pages = res["items"][0]["volumeInfo"]["pageCount"]
        sales = res["items"][0]["saleInfo"]["isEbook"]
        return f"Title: {title} Author: {author}, Description: {description} Páginas: {pages},  Available in ebook?: {sales}"
    
    except KeyError:
        return n
    print(res.url)

results = [get_description(i) for i in x]

print(results)




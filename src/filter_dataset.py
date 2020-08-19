import pandas as pd
from parse import parser 
import re 


result = pd.read_csv("Output/books_clean_dataset.csv")
result = pd.DataFrame(result)


def filter_dataset(x,y):
    """
    Filters the dataset with the year and genre
    """

    filtered = result[(result["year"]== x) & (result["category_name"].str.contains(f"{y}",regex=True,flags= re.IGNORECASE))& (result["rating-avg"]>1)].sort_values(by="rating-avg",ascending=False).head(1)
    return filtered
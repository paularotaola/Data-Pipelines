import src.funciones as fc
import requests
import json
import pandas as pd
import argparse
from parse import parser 


def main():

    args = fc.parser()
    year = args.year
    genre = args.genre
    print (args)
    
    result = pd.read_csv("Output/books_clean_dataset.csv")
    result = pd.DataFrame(result)

    n = fc.output(year, genre)
    if n.empty:
        print("No book recommendation for this genre, please introduce another option")
    
    x = pd.unique(n["isbn10"]).tolist()
    results = [fc.get_description(i) for i in x]
    print(results)
    
    if results == Exception:
        print("")
    
if __name__ == "__main__":
        main()
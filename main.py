import src.funciones as fc
import requests
import json
import pandas as pd
import argparse
from parse import parser 


"""if genre == "novel":
    return "335"
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


def main():

    args = fc.parser()
    year = args.year
    genre = args.genre
    print (args)
    #fc.genres(genre)
    
    result = pd.read_csv("Output/books_output.csv")
    result = pd.DataFrame(result)
    n = fc.output(year, genre)
    x = pd.unique(n["isbn10"]).tolist()
    results = [fc.get_description(i) for i in x]
    print(results)

if __name__ == "__main__":
        main()

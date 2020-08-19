from argparse import ArgumentParser
import argparse


def parser():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Hello, This is your Book Recommendation App. Introduce a year and genre and we will recommend you the best book to read :)")
    
    # Add argument (int)
    parser.add_argument("-y",dest="year", help="Please, insert a year",type=int)

    # Add argument (str)
    parser.add_argument("-g",dest="genre", help="Please, insert a book genre", type=str)

    # Retrieve Arguments
    args = parser.parse_args()
    year = args.year
    genre = args.genre

    # Accessing different variables in args
 
    return args


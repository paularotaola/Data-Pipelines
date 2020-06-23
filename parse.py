from argparse import ArgumentParser
import argparse


def parser():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Book Recommendation App")
    # Add argument (int)
    parser.add_argument("year", help="Insert a number",type=int)
    # Add argument (str)
    parser.add_argument("genre", help="Insert a genre", type=str)

    # Retrieve Arguments
    args = parser.parse_args()
    year = args.year
    gender = args.genre

    # Accessing different variables in args
 
    return args


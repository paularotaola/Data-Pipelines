# Data-Pipelines

## “So many books, so little time…”

![alt libros](Input/books-portada.jpg)

### Overview

The goal of this project is to build a data pipeline that processes the data and produces a result. In this case the result will be a book recommendation based on the genre and year selected by the user.

### Program Workflow

The program will receive two parameters; age and genre and will run the folowwin actions:
* Filter the dataset containing +55.000 books and will return the top book bases on ratings
* Connect with Google Books API to get a description and number of pages of the selected book
* Generate a PDF including the title, author, description and number of pages of the book.

### Example of Program Execution

To run the program, it is necessary to call it from the terminal in the following way: python3 main.py and add the flags with the arguments to search for: “year” (being the year) -and “genre” (being the genre)

Execution example:

> python3 main.py  2010  novel

Valid genres are shown in the list below.

* novel
* poetry
* drama 
* adventure 
* romance 
* thriller
* biographies 
* comic
* science-fiction
* science
* kids
* mental-health


### Resources 

* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html)
* [Python List Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python)
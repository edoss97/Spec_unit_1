### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

from part_4 import my_book_list
from random import choice

def make_dictionary_list(list):
    for book in list:
        title = book['title']
        author = book['author']
        year = book['year']
        rating = book['rating']
        pages = book['pages'] 
        with open("library.txt","a") as file:
            file.write(f"{title}, {author}, {year}, {rating}, {pages} \n")
    return None
 
# def main_menu():
#     question = None
#     while question != "D":
#         question = input("Would you like to A). Add a New Book B). View All Books C). Search For Title D). Exit ")
#         question = question.upper()
#         if question == "A":
#             title = str(input("What is the title of the book? "))
#             author = str(input("Who is the author of the book? "))
#             try:
#                 year = int(input("What year was this book published? "))
#             except:
#                 year = int(input("What year was this book published NUMBER? "))
#             try:    
#                 rating = float(input("What do you rate this book out of 5? "))
#             except: 
#                 rating = float(input("please type your rating out of 5 in NUMBER form? "))
#             try:
#                 pages = int(input("How many pages is this book? "))
#             except:
#                 pages = int(input("please type a NUMBER of pages"))
#             with open("library.txt","a") as f:
#                 f.write(f"{title}, {author}, {year}, {rating}, {pages} \n")
#         elif question == "B":
#             with open("library.txt","r") as f:
#                 f.readlines()
#         elif question == "C":
#             input_title = input("What title? ")
#             for book in my_book_list:
#                 if input_title == book["title"]:
#                     print(book)
# Code here
# with open("library.txt","w") as file:
#     file.write("title, author, year, ratings, pages/n")


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
# def view_books():
#     print("Your books are:\n")
#     with open("library.txt","r") as f:
#         file = f.readlines()

#         for book in file:
#             title, author, year, rating, pages = book.split(", ")

#             print(f" Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

# view_books()

# def book_list_as_dictionaries():
#     dict_books_list = []
#     with open("library.txt", "r") as f:
#         file = f.readlines()
#         for book in file:
#             title, author, year, rating, pages = book.split(", ")
#             dict_books_list.append({
#                 "title": title,
#                 "author": author,
#                 "year": (year),
#                 "rating": (rating),
#                 "pages": (pages)
#             })
#         return dict_books_list
# print(book_list_as_dictionaries())
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def book_list_as_dictionaries(txt_file):
    dict_books_list = []
    with open(txt_file, "r") as f:
        file = f.readlines()
        for book in file:
            title, author, year, rating, pages = book.split(", ")
            dict_books_list.append({
                "title": title,
                "author": author,
                "year": (year),
                "rating": (rating),
                "pages": (pages)
            })
        return dict_books_list

def view_books(txt_file):
    print("Your books are:\n")
    with open(txt_file,"r") as f:
        file = f.readlines()
        for book in file:
            title, author, year, rating, pages = book.split(",")
            print(f" Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")
        input("Press Enter to return to Main Menu")

def highest_ranked(txt_file):
    with open(txt_file,"r") as f:
        file = f.readlines()
        set_best = 0.1
        best_ranked ={}
        for book in file:
            title, author, year, rating, pages = book.split(",")
            rating = float(rating)
            if rating > set_best:
                set_best = rating
                best_ranked = book
        print(f"The best ranked book is: {best_ranked}")
        input("Press Enter to return to Main Menu")

def oldest_book(txt_file):
    with open(txt_file,"r") as f:
        file = f.readlines()
        old_pub_date= 500000.1
        old_book = {}
        for book in file:
            title, author, year, rating, pages = book.split(",")
            year = float(year)
            if year < old_pub_date:
                old_pub_date = year
                old_book = book
        print(f"The Oldest book is: {old_book}")
        input("Press Enter to return to Main Menu")
            
def random_recomendation(txt_file):
     with open(txt_file,"r") as f:
        file = f.readlines()
        book =choice(file)
        print(f"Your reccomendation is: {book}")
        input("Press Enter to return to Main Menu")
    
def book_count(txt_file):
    with open(txt_file,"r") as f:
        file = f.readlines()
        count = 0
        for book in file:
            count = count + 1
        print(f"There are {count} Books!")
        input("Press Enter to return to Main Menu")

def main_menu(txt_file):
    question = None
    while question != "H":
        question = input("Would you like to\nA). Add a New Book\nB). View All Books\nC). Search For Title\nD). Get Highest Ranked Book\nE). Choose Random Book\nF). Total Book Count\nG). Oldest Book\nH). Exit\nChoose Letter:")
        question = question.upper()
        if question == "A":
            title = str(input("What is the title of the book? "))
            author = str(input("Who is the author of the book? "))
            try:
                year = int(input("What year was this book published? "))
            except:
                year = int(input("What year was this book published NUMBER? "))
            try:    
                rating = float(input("What do you rate this book out of 5? "))
            except: 
                rating = float(input("please type your rating out of 5 in NUMBER form? "))
            try:
                pages = int(input("How many pages is this book? "))
            except:
                pages = int(input("please type a NUMBER of pages"))
            title = title.upper()
            with open(txt_file,"a") as f:
                f.write(f"{title}, {author}, {year}, {rating}, {pages} \n")
            print(f"Your Book {title} Has Been Added!")
            input("Press Enter to return to Main Menu")
        elif question == "B":
            view_books(txt_file)
        elif question == "C":
            input_title = input("What title? ")
            input_title = input_title.upper()
            with open(txt_file,"r") as f:
                file = f.readlines()
                for book in file:
                    title, author, year, rating, pages = book.split(",")
                    if input_title == title:
                        print(book)
            input("Press Enter to return to Main Menu")
        elif question == "D":
            highest_ranked(txt_file)
        elif question == "E":
           random_recomendation(txt_file)
        elif question == "F":
           book_count(txt_file)
        elif question == "G":
            oldest_book(txt_file)

if __name__ == "__main__":
    main_menu("library.txt")

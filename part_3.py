my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(dictionary):
    book_string = f"{dictionary['title']} was written by {dictionary['author']} in the year {dictionary['year']} it has {dictionary['pages']} pages in it and was rated {dictionary['rating']}"
    return book_string

print(book_parser(my_book))
# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(dictionary):
    return f"{dictionary['title']}"

def book_author(dictionary):
    return f"{dictionary['author']}"

def book_year(dictionary):
    return f"{dictionary['year']}"

def book_rating(dictionary):
    return f"{dictionary['rating']}"

def book_pages(dictionary):
    return f"{dictionary['pages']}"

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below



def books_2000_plus(list):
    newList = [None]
    for book in list:
        if f"{book['year']}" >= 2000:  
            newList.append(book)
    return newList

def books_before_2000(list):
    newList = [None]
    for book in list:
        if f"{book['year']}" < 2000:  
            newList.append(book)
    return newList

def books_ratings_4plus(list):
    newList = [None]
    for book in list:
        if f"{book['rating']}" >= 4:  
            newList.append(book)
    return newList
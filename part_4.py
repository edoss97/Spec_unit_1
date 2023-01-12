my_book_list = [{
    "title": "THE HUNGER GAMES",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "HARRY POTTER",
    "author": "JK Rowling",
    "year": 1997,
    "rating": 4.52,
    "pages": 450
},
{
    "title": "THE GREAT GATSBY",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "rating": 3.9,
    "pages": 208
},
{
    "title": "OF MICE AND MEN",
    "author": "John Steinbeck",
    "year": 1937,
    "rating": 4.6,
    "pages": 228
},
{
    "title": "TO KILL A MOCKINGBIRD",
    "author": "Harper Lee",
    "year": 1960,
    "rating": 4.85,
    "pages": 185
},
]


### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def new_book():
#     title = input("What is the title of the book? ")
#     author = input("Who is the author of the book? ")
#     year = input("What year was this book published? ")
#     rating = input("What do you rate this book out of 5? ")
#     pages = input("How many pages is this book? ")

#     new_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return new_dictionary

## Step 2 - Type conversion

# Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def new_book():
#     title = str(input("What is the title of the book? "))
#     author = str(input("Who is the author of the book? "))
#     year = int(input("What year was this book published? "))
#     rating = float(input("What do you rate this book out of 5? "))
#     pages = int(input("How many pages is this book? "))


#     new_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return new_dictionary

# print(new_book())
## Step 3 - Error handling

# Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def new_book():
#     title = str(input("What is the title of the book? "))
#     author = str(input("Who is the author of the book? "))
#     year = int(input("What year was this book published? "))
#     try:    
#         rating = float(input("What do you rate this book out of 5? "))
#     except: 
#         rating = float(input("please type your rating out of 5 in NUMBER form? "))
#     try:
#         pages = int(input("How many pages is this book? "))
#     except:
#         pages = int(input("please type a NUMBER of pages"))

#     new_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     my_book_list.append(new_dictionary)
#     return my_book_list

# print(new_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def new_book():
#     title = str(input("What is the title of the book? "))
#     author = str(input("Who is the author of the book? "))
#     try:
#         year = int(input("What year was this book published? "))
#     except:
#         year = int(input("What year was this book published NUMBER? "))
#     try:    
#         rating = float(input("What do you rate this book out of 5? "))
#     except: 
#         rating = float(input("please type your rating out of 5 in NUMBER form? "))
#     try:
#         pages = int(input("How many pages is this book? "))
#     except:
#         pages = int(input("please type a NUMBER of pages"))
#     new_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     my_book_list.append(new_dictionary)
#     print(f"your book {new_dictionary[title]} has been added!")

# def main_menu():
#     question = None
#     while question != "Exit":
#         question = input("Would you like to a). Add a New Book b). View All Books c). Search For Title D. Exit ")
#         if question == "Add a New Book":
#             new_book()
#         elif question == "View All Books":
#             print(my_book_list)
#         elif question == "Search For Title":
#             input_title = input("What title? ")
#             for book in my_book_list:
#                 if input_title == book["title"]:
#                     print(book)
                
#         else:
#             print("Error please try again")

# print(main_menu())

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# def main_menu():
#     question = None
#     while question != "D":
#         question = input("Would you like to A). Add a New Book B). View All Books C). Search For Title D). Exit ")
#         question = question.upper()
#         if question.upper() == "A":
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
#             new_dictionary = {
#                 "title": title,
#                 "author": author,
#                 "year": year,
#                 "rating": rating,
#                 "pages": pages
#                 }
#             my_book_list.append(new_dictionary)
#         elif question.upper() == "B":
#             print(my_book_list)
#         elif question.upper() == "C":
#             input_title = input("What title? ")
#             for book in my_book_list:
#                 if input_title == book["title"]:
#                     print(book)


# main_menu()


import sys
import mysql.connector
from mysql.connector import errorcode

config = {
  "user": "whatabook_user",
  "password": "MySQL8IsGreat!",
  "host": "localhost",
  "database": "whatabook",
  "raise_on_warnings": True
}

def main_menu():
  print("\n --WhatABook Main Menu--")
  print(" 1. View Books\n 2. View Store Locations\n 3. My Account\n 4. Quit")

  try :
      choice = int(input("    Pick a menu option: "))
      
      return choice
  
  except ValueError:
    print("\n Invalid selection, program will end...\n")
  
    sys.exit(0)

def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book")
    
    books = cursor.fetchall()
    
    print("\n -- DISPLAYING BOOK LISTING --")
    
    for book in books:
        print(" Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2]))
        
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store")
    
    locations=cursor.fetchall()

    print("\n -- DISPLAYING STORE LOCATIONS --")
    
    for location in locations:
        print(" Locale: {}\n".format(location[1]))

def validate_user():
    try:
        user_id = int(input('\n   Please enter a customer id: '))

        if user_id < 0 or user_id > 3:
            print("\n Invalid customer number, program will end...\n")
            
            sys.ext(0)

        return user_id
    except ValueError:
        print("\n Invalid number, program will end...\n")
        
        sys.exit(0)

def show_account_menu():

    try:
        print("\n       --Customer Menu --")
        
        print("     1.wishlist\n    2.Add Book\n    3.Back To Main Menu")
        account_option = int(input("     Please make a selection: "))

        return account_option
    except ValueError:
        print("\n Invalid number, program will end...\n")
        
        sys.exit(0)

def show_wishlist(cursor, user_id):
    
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    

    wishlist = cursor.fetchall()

    print("\n  --DISPLAYING WISHLIST ITEMS--")
    
    for book in wishlist:
        print("     Book Name:{}\n      Author:{}\n".format(book[4], book[5]))


def show_books_to_add(cursor,_user_id):
    wishlist_query = ("SELECT book_id, book_name, author,details " 
                    "FROM book "
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    cursor.execute(wishlist_query)
    
    books_to_add = cursor.fetchall()

    print("\n   --DISPLAYING AVAILABLE BOOKS--")

    for book in books_to_add:
        print("     Book ID: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(cursor,_user_id, _book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
   

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = main_menu()
    while user_selection != 4:

    
        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            
            while account_option != 3:

                 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                
                if account_option == 2:

                    
                    show_books_to_add(cursor, my_user_id)

                     
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()  

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")
                account_option = show_account_menu()

        if user_selection < 0 or user_selection > 4:
            print("\n       Invalid option, please try again...")

        user_selection = main_menu()

    print("\n\n Program ending...")
    
#Error handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  ERROR: Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  ERROR: The database is not accessible")
    else:
        print(err)
        
finally:
    """Terminating connection to MySQL """
    db.close()
            
    
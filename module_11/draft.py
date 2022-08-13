menu=0
while menu < 4 :
  print(" 1. View Books\n 2. View Store Location\n 3. View My Account\n 4.Quit")
  menu = int(input("pick a menu option: "))
  if menu == 1:
    import mysql.connector
    from mysql.connector import errorcode
    config = {
      "user": "whatabook_user",
      "password": "MySQL8IsGreat!",
      "host": "127.0.0.1",
      "database": "whatabook",
      "raise_on_warnings": True
    }
    #connect to database
    db = mysql.connector.connect(**config) # connect to the whatabook database
    cursor = db.cursor()
    # select query from the book table
    cursor.execute("SELECT book_id, book_name, author FROM book")
    # get the results from the cursor object
    books = cursor.fetchall()
    print( "\n-- DISPLAYING BOOK RECORDS --")
    # iterate over the books data set and display the results
    for book in books:
        print(" Book ID: {}\n  Book Name: {}\n  Author: {}\n".format(book[0], book[1], book[2]))
  elif menu == 2:
      # select query from the store table
      cursor.execute("SELECT store_id, locale FROM store")
      # get the results from the cursor object
      stores = cursor.fetchall()
      print( "\n-- DISPLAYING STORE RECORDS --")
      # iterate over the stores data set and display the results
      for store in stores:
          print(" Store ID: {}\n  Locale: {}\n".format(store[0], store[1]))
  elif menu == 3:
      print("good")
  elif menu > 3:
    print ("goodbye")
  else:
    print("You picked " + str(menu))

#library management system 
#project 

"""
    1. Add a book
    2. Search for Book
    3. View all Books
    4. Delete a book
"""

"""
    store BookID, Title, Author, Stock (quantity)
"""

"""
    abdul had a pack ad an unpack function
    returned a packed or unpacked record
    packed is a record that has been encoded
    unpacked record is form of a tuble with decoded data
"""

import os
import struct

RECORD_SIZE = 60

def clear_console():
    # Detect the operating system
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for macOS and Linux (posix)
        _ = os.system('clear')


def pack_record(book_id, title, author, stock):
    #i30s20si   the code for packing
    title = title.strip().encode().ljust(30)
    author = author.strip().encode().ljust(20)
    return struct.pack('i30s20si', book_id, title, author, stock)

def unpack_record(record_bytes):
   book_id, title, author, stock = struct.unpack('i30s20si', record_bytes)
   title = title.strip().decode()
   author = author.strip().decode()
   
   return {'BookID' : book_id, 
           'Title' : title, 'Author' : author, 
           'Stock' : stock}


def add_book():
    book_id = int(input('Enter book ID: '))
    title = input('Enter book title: ')
    author = input('Enter Author Name: ')
    stock = int(input('Enter Stock Quantity: '))
    record = pack_record(book_id, title, author, stock)
    with open ('library.dat', 'ab') as file:  #append binary
        file.write(record)
    
def search_book():
    book_id = int(input('Enter Book ID to search: '))
    with open('library.dat', 'rb') as file:
        
        while True:
            record = file.read(RECORD_SIZE)
            if not record:  
                print(f"Book: {book_id} Not Found!")
                break
            else:
                book = unpack_record(record)
                
                if (book['BookID']== book_id):
                    print(book)
                    break


def view_books():
    with open('library.dat', 'rb') as file:
        
        while True:
            record = file.read(RECORD_SIZE)
            if not record:  break
            book = unpack_record(record)
            print (book)


def delete_book():
    book_id = int(input('Enter Book ID to set to delete: '))
    with open('library.dat', 'r+b') as file:
        
        while True:
            record = file.read(RECORD_SIZE)
            if not record:  
                print(f"Book: {book_id} Not Found!")
                break
            else:
                book = unpack_record(record)
                
                if (book['BookID']== book_id):
                    newID = book['BookID']
                    author = book['Author']
                    title = book['Title']
                    stock = 0     #this is the only data that will change
                    
                    new_record = pack_record(newID, title, author, stock)
                    file.seek(RECORD_SIZE*-1, 1)  #move back 60 bytes in this case
                    file.write(new_record)   
                    view_books()
                    break





while True:
    
    print("Journal Manager -- Activity Menu\n")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. View all Books")
    print("4. Delete a Book (set count to zero)")
    print("5. Exit Library Manager\n")
    
    
    selection = int(input("Please enter menu selection: "))

    if (selection == 1):
        add_book()
    elif(selection == 2):
        search_book()
    elif(selection == 3):
        view_books()
    elif(selection == 4):
       delete_book()
    elif(selection == 5):
        print ('Goodbye!')
        break
    else:
        clear_console()
        print("\nPlease enter a valid selection.\n")
        





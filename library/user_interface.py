from .library import Library
from .book import Book
from .file_manager import load_library, save_library

def display_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Books")
    print("4. Search Books by Author")
    print("5. Remove Book")
    print("6. Lend Book")
    print("7. View Lent Books")
    print("8. Return Book")
    print("9. Exit")

def add_book(library):
    title = input("Enter title: ")
    authors = input("Enter authors (comma separated): ").split(',')
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    
    # Validate price input
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Invalid input. The book price should be a floating number.")
    
    # Validate quantity input
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Invalid input. The quantity should be an integer.")
    
    book = Book(title, authors, isbn, year, price, quantity)
    library.add_book(book)
    save_library(library, 'data/books.json')
    print("Book added successfully!")

def view_all_books(library):
    books = library.view_all_books()
    if books:
        for book in books:
            print(book)
    else:
        print("No books available in the library.")

def search_books(library):
    search_term = input("Enter title or ISBN to search: ")
    books = library.search_books(search_term)
    if books:
        for book in books:
            print(book)
    else:
        print("No books found matching the search term.")

def search_books_by_author(library):
    author = input("Enter author name to search: ")
    books = library.search_books_by_author(author)
    if books:
        for book in books:
            print(book)
    else:
        print("No books found for the given author.")

def remove_book(library):
    search_term = input("Enter title or ISBN of the book to remove: ")
    book = library.remove_book(search_term)
    if book:
        save_library(library, 'data/books.json')
        print("Book removed successfully!")
    else:
        print("Book not found!")

def lend_book(library):
    search_term = input("Enter title or ISBN of the book to lend: ")
    borrower = input("Enter borrower's name: ")
    try:
        book = library.lend_book(search_term, borrower)
        if book:
            save_library(library, 'data/books.json')
            print("Book lent successfully!")
        else:
            print("Book not available to lend.")
    except Exception as e:
        print(e)

def view_lent_books(library):
    lent_books = library.view_lent_books()
    books_exist = False 

    for book, borrowers in lent_books.items():
        if borrowers:  
            if book != 'None':  
                print(f"{book} lent to {', '.join(borrowers)}")
                books_exist = True  

    if not books_exist:
        print("No books have been lent out.")


def return_book(library):
    search_term = input("Enter title or ISBN of the book to return: ")
    borrower = input("Enter borrower's name: ")
    book = library.return_book(search_term, borrower)
    if book:
        save_library(library, 'data/books.json')
        print("Book returned successfully!")
    else:
        print("Book not found or was not lent to this borrower.")

def main():
    library = load_library('data/books.json')
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_all_books(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            search_books_by_author(library)
        elif choice == '5':
            remove_book(library)
        elif choice == '6':
            lend_book(library)
        elif choice == '7':
            view_lent_books(library)
        elif choice == '8':
            return_book(library)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

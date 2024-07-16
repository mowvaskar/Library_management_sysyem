# Library Management System

This project is a Command Line Interface (CLI) based Library Management System developed in Python. The system allows users to manage a collection of books by adding, viewing, searching, lending, and returning books. All changes to the library are persisted in a JSON file, ensuring that the state of the library is maintained across program executions.

## Features

1. **Add Books**: Add new books to the library with details like title, authors, ISBN, publishing year, price, and quantity.
2. **View Books**: Display all the books available in the library.
3. **Search Books**: Search for books by title or ISBN.
4. **Search Books by Author**: Search for books by author names.
5. **Remove Books**: Remove books from the library by searching with title or ISBN.
6. **Lend Books**: Lend books to borrowers, reducing the quantity of available books.
7. **View Lent Books**: View all the books that have been lent out and their respective borrowers.
8. **Return Books**: Return books to the library, updating the quantity accordingly.
9. **Persistent Storage**: All the information is saved in a JSON file (`books.json`), which ensures that the library's state is persistent.





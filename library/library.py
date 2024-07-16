import json
from .book import Book

class Library:
    def __init__(self):
        self.books = []
        self.lent_books = {}

    def add_book(self, book):
        self.books.append(book)
        self.update_json_file()

    def view_all_books(self):
        return self.books

    def search_books(self, search_term):
        return [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.isbn.lower()]

    def search_books_by_author(self, author):
        return [book for book in self.books if any(author.lower() in auth.lower() for auth in book.authors)]

    def remove_book(self, search_term):
        book = None
        for b in self.books:
            if b.isbn == search_term or b.title == search_term:
                book = b
                break

        if book:
            self.books.remove(book)
            # Remove from lent_books if it exists
            if book.isbn in self.lent_books:
                del self.lent_books[book.isbn]
            self.update_json_file()
            return book
        else:
            return None

    def update_json_file(self):
        data = {
            "books": [book.__dict__ for book in self.books],
            "lent_books": self.lent_books
        }
        with open('data/books.json', 'w') as file:
            json.dump(data, file, indent=4)

    def lend_book(self, search_term, borrower):
        for book in self.books:
            if (search_term.lower() in book.title.lower() or search_term.lower() in book.isbn.lower()) and book.quantity > 0:
                book.quantity -= 1
                if book.isbn not in self.lent_books:
                    self.lent_books[book.isbn] = []
                self.lent_books[book.isbn].append(borrower)
                self.update_json_file()
                return book
        return None

    def view_lent_books(self):
        lent_books_info = {self._get_book_by_isbn(isbn).title: borrowers for isbn, borrowers in self.lent_books.items() if borrowers and self._get_book_by_isbn(isbn)}
        return lent_books_info

    def return_book(self, search_term, borrower):
        for isbn, borrowers in self.lent_books.items():
            book = self._get_book_by_isbn(isbn)
            if book and (search_term.lower() in book.title.lower() or search_term.lower() in book.isbn.lower()) and borrower in borrowers:
                book.quantity += 1
                borrowers.remove(borrower)
                if not borrowers:
                    del self.lent_books[isbn]
                self.update_json_file()
                return book
        return None

    def save_to_file(self, filepath):
        data = {
            "books": [book.__dict__ for book in self.books],
            "lent_books": {isbn: borrowers for isbn, borrowers in self.lent_books.items() if borrowers}
        }
        with open(filepath, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filepath):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data.get("books", [])]
                self.lent_books = {isbn: borrowers for isbn, borrowers in data.get("lent_books", {}).items()}
        except FileNotFoundError:
            pass

    def _get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

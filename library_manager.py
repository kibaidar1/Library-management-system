import json
import os
from typing import Any

from models import Book


class LibraryManager:
    """
    A class to manage a library's collection of books.

    Attributes:
    storage_file (str): The file where book data is stored. Defaults to 'library.json'.
    books (list): A list of dictionaries representing books in the library.

    Methods:
    _create_storage_file(): Creates a new storage file if it doesn't exist.
    _generate_id(): Generates a unique ID for a new book.
    _load_books(): Loads book data from the storage file.
    _save_books(): Saves book data to the storage file.
    add_book(title: str, author: str, year: int) -> dict: Adds a new book to the library.
    delete_book(book_id: int) -> bool: Deletes a book from the library by its ID.
    find_books(query: str) -> list: Finds books in the library based on a search query.
    get_books(): Returns a list of all books in the library.
    change_book_status(book_id: int, new_status: str) -> Book | bool: Changes the status of a book.
    """

    def __init__(self, storage_file: str = 'library.json'):
        self.storage_file = storage_file
        self.books = self._load_books()

    def _create_storage_file(self):
        with open(self.storage_file, 'w') as f:
            f.write('[]')

    def _generate_id(self) -> int:
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                books = json.load(f)
                if books:
                    return max(book['id'] for book in books) + 1
        return 1

    def _load_books(self) -> list[dict[str, Any]]:
        if not os.path.exists(self.storage_file):
            self._create_storage_file()
        with open(self.storage_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_books(self):
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> dict[str, Any]:
        book = Book(self._generate_id(), title, author, year)
        self.books.append(book.to_dict())
        self._save_books()
        return book.to_dict()

    def delete_book(self, book_id: int) -> bool:
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                self._save_books()
                return True
        return False

    def find_books(self, query: str):
        return [book for book in self.books
                if query.lower() in (book['title'] + book['author'] + str(book['year'])).lower()]

    def get_books(self):
        return self.books

    def change_book_status(self, book_id: int, new_status: str) -> dict | bool:
        for book in self.books:
            if book['id'] == book_id:
                validated_book = Book(book['id'], book['title'], book['author'], book['year'], new_status)
                book['status'] = validated_book.status
                self._save_books()
                return book
        return False


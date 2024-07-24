import json
import os
from typing import Dict, Any

from models import Book


class LibraryManager:
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

    def _load_books(self):
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

    def find_books(self, query: str) -> list[Book]:
        return [book for book in self.books
                if query.lower() in (book['title'] + book['author'] + str(book['year'])).lower()]

    def get_books(self):
        return self.books

    def change_book_status(self, book_id: int, new_status: str) -> Book | bool:
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = new_status
                self._save_books()
                return book
        return False


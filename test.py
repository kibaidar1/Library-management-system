import os
import unittest
from library_manager import LibraryManager, Book


class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.library = LibraryManager('test_library.json')
        self.book = self.library.add_book('Test Book', 'Test Author', 2022)

    def tearDown(self):
        os.remove('test_library.json')

    def test_add_book_saves_to_file(self):
        # Given
        book_title = 'Test Book'
        author = 'Test Author'
        year = 2022

        # When
        book = self.library.add_book(book_title, author, year)

        # Then
        self.assertEqual(book['title'], book_title)
        self.assertEqual(book['author'], author)
        self.assertEqual(book['year'], year)

    def test_delete_book_removes_from_file(self):
        # Given
        book_id = self.book['id']

        # When
        deleted = self.library.delete_book(book_id)

        # Then
        self.assertTrue(deleted)
        self.assertNotIn(self.book, self.library.get_books())

    def test_get_books_returns_all_books(self):
        # When
        books = self.library.get_books()

        # Then
        self.assertIn(self.book, books)
        self.assertEqual(len(books), 1)

    def test_find_books_returns_matching_books(self):
        # Given
        query = 'Test'

        # When
        matching_books = self.library.find_books(query)

        # Then
        self.assertIn(self.book, matching_books)
        self.assertEqual(len(matching_books), 1)

    def test_change_book_status_updates_status_and_list(self):
        # Given
        new_status = 'на руках'

        # When
        updated_book = self.library.change_book_status(self.book['id'], new_status)

        # Then
        self.assertEqual(updated_book['status'], new_status)
        self.assertEqual(self.library.get_books()[0]['status'], new_status)


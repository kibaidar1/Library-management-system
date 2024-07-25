from dataclasses import dataclass
from datetime import datetime


class Book:
    """
    A class representing a book with properties and methods.

    Attributes:
    _id (int): The unique identifier of the book.
    title (str): The title of the book.
    author (str): The author of the book.
    year (int): The publication year of the book.
    status (str): The availability status of the book. Defaults to 'в наличии'.

    Methods:
    to_dict(): Returns a dictionary representation of the book object.
    """

    def __init__(self, id: int, title: str, author: str, year: int, status: str = 'в наличии'):
        self._id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or value == '':
            raise ValueError("title must be a string and not null")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or value == '':
            raise ValueError("author must be a string and not null")
        self._author = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value == '':
            raise ValueError("year must be an integer and not null")
        if value > datetime.now().year:
            raise ValueError("year must be less than or equal to current year")
        self._year = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ['в наличии', 'на руках']:
            raise ValueError("status must be 'в наличии' or 'на руках'")
        self._status = value

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the book object.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

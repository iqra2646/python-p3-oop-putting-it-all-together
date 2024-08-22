#!/usr/bin/env python3

import sys

class Book:
    def __init__(self, title, page_count):
        """
        Initialize the Book class with title and page_count.
        """
        self.title = title
        self._page_count = None  # Private variable for page_count
        self.page_count = page_count  # Use the setter method to handle validation

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer", file=sys.stdout)
        else:
            self._page_count = value

    def get_description(self):
        """
        Return a description of the book in the form of a string.
        """
        return f"'{self.title}' with {self.page_count} pages"

    def is_long(self):
        """
        Determine if the book is long based on the number of pages.
        """
        return self.page_count > 300

    def turn_page(self):
        """
        Simulates turning the page of the book and outputs a message.
        """
        print("Flipping the page...wow, you read fast!")

#!/usr/bin/env python3
import sys

class Shoe:
    def __init__(self, brand, size, color):
        """
        Initialize the Shoe class with brand, size, and color.
        """
        self.brand = brand
        self.color = color
        self.set_size(size)  # Use the setter to initialize size
        self.condition = "New"  # Initialize condition

    def set_size(self, size):
        """
        Set the size of the shoe, with validation to ensure it's an integer.
        """
        if not isinstance(size, int):
            print("size must be an integer", file=sys.stdout)
            self._size = None  # Private attribute to store size
        else:
            self._size = size
    
    @property
    def size(self):
        """
        Getter for the size property.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter for the size property with validation to ensure it's an integer.
        """
        if not isinstance(value, int):
            print("size must be an integer", file=sys.stdout)
        else:
            self._size = value

    def cobble(self):
        """
        Print a message and set the shoe condition to 'New'.
        """
        print("Your shoe is as good as new!", file=sys.stdout)
        self.condition = "New"
    
    def get_description(self):
        """
        Return a description of the shoe in the form of a string.
        """
        return f"{self.brand} shoe of size {self.size} and color {self.color}"

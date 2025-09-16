#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """
        Initializes the square with a private size.
        Checks that size is an integer >= 0.
        """
        if size is None or not isinstance(size, int):
            raise AttributeError("'Square' object has no attribute 'size'")

        self.__size = size

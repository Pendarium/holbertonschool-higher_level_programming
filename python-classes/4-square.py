#!/usr/bin/python3
"""Module defining a class Square with size validation and area computation.
"""


class Square:
    """Represents a square with a given size.

    Attributes:
        __size (int): La taille du côté du carré (privée).
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): La taille du côté du carré (par défaut 0).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: La taille actuelle du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square using the '#' character.

        If the size of the square is 0, prints an empty line.

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.size)

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

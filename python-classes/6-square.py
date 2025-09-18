#!/usr/bin/python3
"""Module defining a class Square with size
validation, position, and area computation.
"""


class Square:
    """Represents a square defined by its size and position.

    Private attributes:
        __size (int): La taille du côté du carré.
        __position (tuple): La position du carré sous forme de tuple (x, y).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): La taille du côté du carré (par défaut 0).
            position (tuple): La position du carré (par défaut (0, 0)).

        Raises:
            TypeError: Si size n'est pas un entier ou si position n'est pas un
                tuple de deux entiers positifs.
            ValueError: Si size est négatif.
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Get the current position of the square.

        Returns:
            tuple: La position (x, y) du carré.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): Nouveau tuple de position (x, y).

        Raises:
            TypeError: Si value n'est pas un tuple de deux entiers positifs.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: La taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): Nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute and return the area of the square.

        Returns:
            int: L'aire (taille²) du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character with respect to position.

        If size is 0, prints an empty line.
        Position defines the number of spaces (horizontal offset) and
        new lines (vertical offset) before printing the square.
        """
        if self.__size == 0:
            print()
            return

        # Décalage vertical
        for _ in range(self.__position[1]):
            print()

        # Impression de chaque ligne du carré avec décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

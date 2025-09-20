#!/usr/bin/python3
"""Module that defines the Rectangle class.
"""


class Rectangle:
    """Class Rectangle: représente un rectangle avec largeur et hauteur.
    
    Attributes:
        __width (int): largeur du rectangle (privé)
        __height (int): hauteur du rectangle (privé)
    """

    def __init__(self, width=0, height=0):
        """Initialise un nouvel objet Rectangle.

        Args:
            width (int): largeur du rectangle (valeur par défaut 0)
            height (int): hauteur du rectangle (valeur par défaut 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter de l'attribut width.

        Returns:
            int: la largeur actuelle du rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter de l'attribut width.

        Args:
            value (int): nouvelle largeur du rectangle

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter de l'attribut height.

        Returns:
            int: la hauteur actuelle du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter de l'attribut height.

        Args:
            value (int): nouvelle hauteur du rectangle

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.

    Classe représentant un rectangle, héritée de BaseGeometry.
    Cette classe valide les dimensions données et les stocke
    comme attributs privés.

    Attributes:
        __width (int): Largeur du rectangle.
        __height (int): Hauteur du rectangle.

    Methods:
        __init__(self, width, height):
            Initialise un rectangle en validant les dimensions.
    """

    def __init__(self, width, height):
        """
        Initialise un nouvel objet Rectangle avec validation.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Raises:
            TypeError: Si width ou height ne sont pas des entiers.
            ValueError: Si width ou height sont inférieurs ou égaux à 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

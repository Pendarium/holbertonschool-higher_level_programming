#!/usr/bin/python3
"""
Module: 9-rectangle

Ce module définit une classe Rectangle qui hérite de BaseGeometry.
Il permet de créer des rectangles avec validation des dimensions
et de calculer leur aire.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle héritée de BaseGeometry.

    Cette classe représente un rectangle défini par une largeur
    et une hauteur, toutes deux validées comme entiers strictement
    positifs via la méthode héritée integer_validator.

    Attributs privés :
        __width (int): Largeur du rectangle.
        __height (int): Hauteur du rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un objet Rectangle avec des dimensions valides.

        Args:
            width (int): La largeur du rectangle.
            height (int): La hauteur du rectangle.

        Raises:
            TypeError: Si width ou height ne sont pas des entiers.
            ValueError: Si width ou height sont <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l’aire du rectangle.

        Returns:
            int: L’aire calculée (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation lisible du rectangle.

        Returns:
            str: Description du rectangle au
            format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

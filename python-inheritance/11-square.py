#!/usr/bin/python3
"""
Module defining the Square class.

Module:
    Square class implementation inheriting from Rectangle.

Description:
    Ce module définit la classe Square qui hérite de Rectangle.
    Il permet de créer des carrés avec une taille validée,
    garantissant que la largeur et la hauteur sont identiques
    et strictement positives.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.

    Classe représentant un carré, héritée de la classe Rectangle.
    La taille (size) est validée comme un entier strictement positif
    et stockée comme un attribut privé.

    Args:
        size (int): La taille du carré (largeur et hauteur).

    Raises:
        TypeError: Si size n'est pas un entier.
        ValueError: Si size est inférieur ou égal à 0.

    Attributes:
        __size (int): La taille privée du carré.

    Methods:
        __init__(self, size):
            Initialise un carré avec une taille donnée,
            valide la taille et utilise le constructeur de Rectangle
            pour initialiser largeur et hauteur.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcule l'aire du carré."""
        return self.__size ** 2

    def __str__(self):
        """Retourne la description formatée du carré."""
        return f"[Square] {self.__size}/{self.__size}"

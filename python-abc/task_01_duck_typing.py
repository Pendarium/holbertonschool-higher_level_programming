#!/usr/bin/env python3

"""
Module providing shape classes and a utility
function to display shape information.

Ce module définit une classe abstraite Shape
ainsi que ses implémentations concrètes
Circle et Rectangle. Il inclut également une
fonction utilitaire pour afficher l'aire
et le périmètre des formes, en utilisant
le concept de duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.

    Classe de base abstraite pour les formes géométriques. 
    Elle impose l’implémentation des méthodes area() et perimeter().
    """

    @abstractmethod
    def area(self):
        """Return the area of the shape.

        Retourne l’aire de la forme.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape.

        Retourne le périmètre de la forme.
        """
        pass


class Circle(Shape):
    """
    Circle shape defined by its radius.

    Représente un cercle défini par son rayon.
    """

    def __init__(self, radius):
        """Initialize the circle with a given radius.

        Initialise le cercle avec un rayon donné.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.

        Calcule l’aire du cercle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Calcule le périmètre (circonférence) du cercle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape defined by width and height.

    Représente un rectangle défini par sa largeur et sa hauteur.
    """

    def __init__(self, width, height):
        """Initialize the rectangle with width and height.

        Initialise le rectangle avec une largeur et une hauteur.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Calcule l’aire du rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Calcule le périmètre du rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.

    Affiche l’aire et le périmètre d’une forme, en utilisant le duck typing.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

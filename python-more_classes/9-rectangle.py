#!/usr/bin/python3
"""Module that defines the Rectangle class.
"""


class Rectangle:
    """
    Classe Rectangle : représente un rectangle avec largeur et hauteur.

    Class Attributes:
        number_of_instances (int): Nombre d'instances actives de Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise un nouvel objet
        Rectangle et incrémente le compteur d'instances.

        Args:
            width (int): Largeur du rectangle (par défaut 0)
            height (int): Hauteur du rectangle (par défaut 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter de l'attribut width.

        Returns:
            int: La largeur actuelle du rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de l'attribut width.

        Args:
            value (int): Nouvelle largeur du rectangle

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de l'attribut height.

        Returns:
            int: La hauteur actuelle du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de l'attribut height.

        Args:
            value (int): Nouvelle hauteur du rectangle

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: Aire du rectangle (largeur * hauteur)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Périmètre du rectangle,
            ou 0 si largeur ou hauteur est nulle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Retourne la représentation graphique
        du rectangle avec le caractère #.

        Returns:
            str: Chaîne représentant le rectangle,
            ou chaîne vide si width ou height est 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        line = []
        symbol = str(self.print_symbol)
        for _ in range(self.__height):
            line.append(symbol * self.__width)
        return "\n".join(line)

    def __repr__(self):
        """
        Retourne une chaîne représentant le rectangle
        pour recréer une nouvelle instance.

        Returns:
            str: Chaîne au format 'Rectangle(width, height)'
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Affiche un message lors de la suppression d'une instance
        et décrémente le compteur d'instances.

        Returns:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne le plus grand basé sur l'aire.

        Args:
            rect_1 (Rectangle): Premier rectangle à comparer.
            rect_2 (Rectangle): Deuxième rectangle à comparer.

        Raises:
            TypeError: Si rect_1 n'est pas une instance de Rectangle.
            TypeError: Si rect_2 n'est pas une instance de Rectangle.

        Returns:
            Rectangle: Le rectangle ayant la plus grande aire,
                    ou rect_1 si les deux ont la même aire.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """
        Crée un nouveau rectangle avec largeur et hauteur égales.

        Args:
            size (int): Taille de la largeur et hauteur (par défaut 0).

        Returns:
            Rectangle: Nouvelle instance de Rectangle carrée.
        """
        return cls(size, size)

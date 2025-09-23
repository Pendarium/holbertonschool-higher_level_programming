#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """
    Represents the base geometry.

    Cette classe sert de base pour les classes géométriques.

    Methods:
        area():
            Raises:
                Exception: area() is not implemented.
            Description:
                Méthode à surcharger, lève une exception si non implémentée.

        integer_validator(name, value):
            Args:
                name (str): Le nom de la variable à valider.
                value (int): La valeur à valider.
            Raises:
                TypeError: Si value n'est pas un entier.
                ValueError: Si value est inférieur ou égal à 0.
            Description:
                Valide que value est un entier strictement positif.
    """

    def area(self):
        """
        Raises:
            Exception: area() is not implemented.
        
        Description:
            Lève une exception pour indiquer que
            la méthode doit être implémentée 
            dans une sous-classe.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.

        Description:
            Valide que la valeur est un entier strictement supérieur à zéro. 
            Sinon, lève une exception adaptée avec un message personnalisé.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

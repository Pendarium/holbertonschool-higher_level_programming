#!/usr/bin/env python3
"""
Script demonstrating the use of an abstract base class (ABC) in Python.

Ce script montre comment créer une classe abstraite
`Animal` en Python à l'aide du module `abc`.
Deux classes dérivées, `Dog` et `Cat`, implémentent
la méthode abstraite `sound` pour retourner
des sons caractéristiques ("Bark" et "Meow").
Ce type de structure permet d'assurer que toutes
les classes dérivées respectent une interface
commune définie par la classe de base.

Usage :
    Exécutez ce script directement pour voir
    les sons produits par un chien et un chat.

Auteur : TonNom
Date : 2025-09-25
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    All subclasses must implement the sound() method to define the
    characteristic sound of the animal.
    """

    @abstractmethod
    def sound(self):
        """
        Return the sound made by the animal.

        This method must be implemented by all subclasses.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.

    Implements the sound() method to return "Bark".
    """

    def sound(self):
        """
        Return the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.

    Implements the sound() method to return "Meow".
    """

    def sound(self):
        """
        Return the sound made by a cat.
        """
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    print(dog.sound())  # Output: Bark
    print(cat.sound())  # Output: Meow

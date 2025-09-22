#!/usr/bin/python3
"""
Module contenant la classe MyList.

Cette classe hérite de list et ajoute une méthode
pour afficher la liste triée en ordre croissant.
"""


class MyList(list):
    """
    Classe héritant de list avec une méthode pour afficher la liste triée.

    Methods:
        print_sorted(): Affiche la liste triée en ordre croissant.
    """

    def print_sorted(self):
        """
        Affiche la liste triée en ordre croissant.

        Args:
            self: Instance de la classe MyList.

        Returns:
            None
        """
        if isinstance(self, int):
            if self < 0:
                print(sorted(self))
        else:
            print(sorted(self))

#!/usr/bin/python3
"""
Module 0-lookup

Ce module contient la fonction `lookup` qui retourne
la liste des attributs et méthodes disponibles pour un objet.
"""


def lookup(obj):
    """
    Renvoie la liste des attributs et des
    méthodes disponibles pour un objet donné.

    Args:
        obj: L'objet dont on veut obtenir la liste des attributs et méthodes.

    Returns:
        list: Une liste de chaînes contenant les noms
              des attributs et méthodes accessibles.
    """
    return dir(obj)

#!/usr/bin/python3
"""
Module: is_same_class

Description:
    Module contenant une fonction pour vérifier si un objet
    est exactement une instance d'une classe donnée.
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance d'une classe donnée.

    Args:
        obj (object): L'objet à vérifier.
        a_class (type): La classe à comparer.

    Returns:
        bool: True si l'objet est exactement une instance de la classe,
              False sinon.
    """
    if obj.__class__ != a_class:
        return False
    else:
        return True

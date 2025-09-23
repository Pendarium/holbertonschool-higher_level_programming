#!/usr/bin/python3
"""
Module: is_kind_of_class

Description:
    Module contenant une fonction qui vérifie si un objet est
    une instance d'une classe spécifiée ou d'une de ses sous-classes.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of
    the specified class or its subclasses.

    Description:
        Vérifie si un objet est une instance de la classe spécifiée ou
        d'une classe héritée (sous-classe) de cette classe.

    Args:
        obj (object): L'objet à vérifier.
        a_class (type): La classe à comparer.

    Returns:
        bool: True si l'objet est une instance de
              la classe ou de ses sous-classes,
              False sinon.
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True

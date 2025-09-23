#!/usr/bin/python3
"""
Module: inherits_from

Description:
    Module contenant une fonction qui vérifie si un objet est une instance
    d'une sous-classe (directe ou indirecte) d'une classe spécifiée.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a subclass of the specified class.

    Description:
        Vérifie si un objet est une instance d'une classe qui hérite
        (directement ou indirectement) de la classe spécifiée, sans être
        une instance directe de cette classe.

    Args:
        obj (object): L'objet à vérifier.
        a_class (type): La classe de référence.

    Returns:
        bool: True si l'objet hérite de la classe, False sinon.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False

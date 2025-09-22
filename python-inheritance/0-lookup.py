#!/usr/bin/python3

def lookup(obj):
    """
    Renvoie la liste des attributs et des
    méthodes disponibles pour un objet donné.

    Args:
        obj: L'objet dont on veut obtenir la liste des attributs et méthodes.

    Returns:
        list: Une liste de chaînes contenant
              les noms des attributs et méthodes accessibles.
    """
    return dir(obj)
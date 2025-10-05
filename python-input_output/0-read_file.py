#!/usr/bin/python3
"""Module contenant la fonction read_file qui lit et affiche un fichier texte UTF-8."""

def read_file(my_file_0=""):
    """Lit un fichier texte (UTF8) et l’affiche sur la sortie standard."""
    with open(my_file_0, encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""
This module contains a function that write some text
in a file.
"""


def write_file(filename="", text=""):
    """
    Writes some text in a specific file.
    File is created if does'nt exist.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        nb_written = file.write(text)
    return nb_written

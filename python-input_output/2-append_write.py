#!/usr/bin/python3
"""
This module contains a function that append a file
"""


def append_write(filename="", text=""):
    """
    This function append some text in a file
    """
    with open(filename, 'a', encoding="utf-8") as file:
        written = file.write(text)
    return written

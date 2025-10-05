#!/usr/bin/python3
"""
This module contains a unfction that create
objects from json files
"""
import json


def load_from_json_file(filename):
    """
    function that create and object from
    a json file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
    # ne pas oublier de quand utilise la méthode .load(s)

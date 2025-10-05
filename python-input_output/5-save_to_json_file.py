#!/usr/bin/python3
"""
This module contains function that
saves object into strings
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function write object turned into a string
    into a json file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)

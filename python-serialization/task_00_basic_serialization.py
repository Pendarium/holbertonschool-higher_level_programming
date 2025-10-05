#!/usr/bin/python3
"""
This module contains functions to serialize or
deserialize objects and save them into
a file (or load them from a file)
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    This functions serialize an object and store the
    result into a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(data, file)


def load_and_deserialize(filename):
    """
    This function deserialize an object from a file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

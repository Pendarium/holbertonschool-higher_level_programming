#!/usr/bin/python3
"""
Module contains a function that create
object from a string
"""
import json


def from_json_string(my_str):
    """
    This function convert a string
    into an object
    """
    return json.loads(my_str)

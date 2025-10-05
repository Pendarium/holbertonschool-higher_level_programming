#!/usr/bin/python3
"""
This module contains a function
that turns an object into a string
representation
"""
import json


def to_json_string(my_obj):
    """
    Convert an object into a string
    representation
    """
    return json.dumps(my_obj)

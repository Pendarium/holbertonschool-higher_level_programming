#!/usr/bin/python3
"""
This module contains a function that
gives the dict representation fo an
object so it can be serialized
"""


def class_to_json(obj):
    """
    This function turns an object
    into his dict representation in order
    to serialize it
    """
    return obj.__dict__

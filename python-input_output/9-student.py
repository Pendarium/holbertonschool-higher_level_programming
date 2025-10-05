#!/usr/bin/python3
"""
This module contains the representation
of a student
"""


class Student:
    """
    This class si a representation of a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function gives the dict representation
        of a student
        """
        return self.__dict__

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

    def to_json(self, attrs=None):
        """
        This function gives the dict representation
        of a student
        """
        if attrs is not None:
            obj_dict = {}
            for keys in self.__dict__:
                for attributes in attrs:
                    if attributes == keys:
                        obj_dict[attributes] = self.__dict__[keys]
            return obj_dict
        return self.__dict__

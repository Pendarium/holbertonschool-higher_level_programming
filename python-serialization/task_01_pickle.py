#!/usr/bin/python3

"""
This module contains an object
 to train on serialization
 and deserialization
 """
import pickle


class CustomObject:
    """
    This class don't represent anything
    but shows how to create serialization
    and deserialization using pickle
    module
    """
    @classmethod
    def deserialize(cls, filename):
        """
        Recreate an object from
        the binary file containing
        the serialized object
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Serialize and object in binary
        and stores it in a file
        """
        with open(filename, 'wb') as file:
            return pickle.dump(self, file)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

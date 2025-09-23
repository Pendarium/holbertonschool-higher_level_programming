#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represent base geometry.

    This class serves as a base for geometry-related classes.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

#!/usr/bin/python3
"""
This module defines the function matrix_divided,
which divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): List of lists of integers or floats.
        div (int or float): Number to divide the matrix elements by.

    Returns:
        list: New matrix with elements divided and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if (
        not isinstance(matrix, list) or not matrix or
        not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

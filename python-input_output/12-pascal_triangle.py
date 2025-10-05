#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle.

The Pascal's triangle is a triangular array of binomial coefficients.
Each number is the sum of the two directly above it in the previous row.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Each row of Pascal's triangle represents the binomial coefficients
    for successive powers of (a + b)^n.

    Args:
        n (int): The number of rows of Pascal’s triangle to generate.

    Returns:
        list[list[int]]: A list of lists of integers representing
        Pascal's triangle up to row n.
        Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

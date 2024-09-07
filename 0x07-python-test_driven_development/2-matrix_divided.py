#!/usr/bin/python3
"""
Divide Matrix Module
"""


def matrix_divided(matrix, div):
    """
    Matrix Divided:
        Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix where each element is an int or float.
        div (int, float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers, or
        if rows are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with each element divided by div,
        rounded to 2 decimal places.
    """

    # Check if matrix is a list of lists and each element is an int or float
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, (int, float))
                for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")

    # Check if all rows are of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]

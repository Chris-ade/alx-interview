#!/usr/bin/python3
"""
Returns a list representing a pascal's triangle
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers printing the Pascal's triangle of n.

    Parameters:
    n (int): The number of rows of the Pascal's triangle

    Returns:
    list of lists of integers: Representing the Pascal's triangle of n.
    If n <= 0, returns an empty list.
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

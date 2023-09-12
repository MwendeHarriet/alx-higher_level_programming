#!/usr/bin/python3
"""This module returns a list of lists of integers
    representing the Pascal’s triangle of n."""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        pas_row = triangle[i - 1]
        add_row = [1]
        for j in range(1, i):
            add_row.append(pas_row[j - 1] + pas_row[j])
        add_row.append(1)
        triangle.append(add_row)
    return triangle

#!/usr/bin/python3
"""This module reads and prints a file."""


def read_file(filename=""):
    """Reads and prints contents of a file.
    Args:
        filename (str): The name of the text file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

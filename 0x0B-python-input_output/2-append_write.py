#!/usr/bin/python3
"""This module appends a string at the end of a text file (UTF8)
    and returns the number of characters added."""


def append_write(filename="", text=""):
    """
    Adds a string to the end of a file.
    Args:
        filename (str): The name of the file.
        text (str): The string to be appended to the file.
    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as ifile:
        return ifile.write(text)

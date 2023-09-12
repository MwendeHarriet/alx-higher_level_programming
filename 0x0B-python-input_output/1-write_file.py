#!/usr/bin/python3
"""This module writes a string to a text file (UTF8) and
    returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Writes a string to a file.
    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as ifile:
        return ifile.write(text)

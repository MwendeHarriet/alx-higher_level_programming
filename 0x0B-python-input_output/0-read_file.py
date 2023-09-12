#!/usr/bin/python3
"""This module reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Reads and prints contents of a file.
    Args:
        filename (str): The name of the text file.
    """
    with open(filename, 'r', encoding='utf-8') as ifile:
        print(ifile.read(), end="")

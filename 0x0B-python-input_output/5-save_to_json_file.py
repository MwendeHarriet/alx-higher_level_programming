#!/usr/bin/python3
"""The module  writes an Object to a text file, using a
    JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a file withJSON.
    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file.
    """
    with open(filename, "w") as ifile:
        json.dump(my_obj, ifile)

#!/usr/bin/python3
"""This module  returns an object (Python data structure)
    represented by a JSON string."""


import json


def from_json_string(my_str):
    """
    Returns python data struct.
    Args:
        my_obj: The json to be converted.
    Returns:
        str: The python data struct.
    """
    return json.loads(my_str)

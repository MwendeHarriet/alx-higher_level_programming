#!/usr/bin/python3
"""This module returns the JSON representation of an object (string)."""


import json


def to_json_string(my_obj):
    """
    Returns JSON representation.
    Args:
        my_obj: The obj to be converted to a JSON string.
    Returns:
        str: The JSON representation of an  object.
    """
    return json.dumps(my_obj)

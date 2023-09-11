#!/usr/bin/python3
"""This module  returns True if the object is
    an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    This checks if obj is the same class of a_clas
    Args:
        obj: object
        a_class: class
    Returns:
        bool: True or False
    """
    return type(obj) == a_class

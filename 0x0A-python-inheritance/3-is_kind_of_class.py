#!/usr/bin/python3
"""This module checks if the object is an instance of or if
    the object is an instance of a class that inherited from
    the specified class"""


def is_kind_of_class(obj, a_class):
    """
    Checks the long ramble above.
    Args:
        obj: object
        a_class: class
        Returns:
            bool: True or False
    """
    return isinstance(obj, a_class)

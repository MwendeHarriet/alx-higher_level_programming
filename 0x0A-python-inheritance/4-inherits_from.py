#!/usr/bin/python3
"""This module if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """
    The fuction doing the documentation above.
    Args:
        obj: object
        a_class: class
    Returns:
    bool: True or False
    """
    if type(obj) == a_class:
        return (False)
    return isinstance(obj, a_class)

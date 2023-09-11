#!/usr/bin/python3
"""This module defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """
    This function adds a new attribute to an object if possible.
    Args:
        obj (any): object to add an attribute to
        att (str): name of the attribute to add to object
        value (any): value of attribute
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

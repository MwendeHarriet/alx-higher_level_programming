#!/usr/bin/python3
"""This module returns the list of available attributes
    and methods of an object."""


def lookup(obj):
    """
    Returns a lis of availa-ble attr and methods of an obj.
    Args:
        obj
    Returns:
        list
    """
    return dir(obj)

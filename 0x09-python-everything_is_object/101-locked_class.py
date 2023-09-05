#!/usr/bin/python3
""" This module defines a Locked class with no class or object attribute.
    It prevents dynamically creating new instance attributes except if
    the new instance attribute is called first_name."""


class LockedClass:
    """ LockedClass """
    __slots__ = ['first_name']

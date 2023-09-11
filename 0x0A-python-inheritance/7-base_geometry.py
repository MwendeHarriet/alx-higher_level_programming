#!/usr/bin/python3
"""This module writes class BaseGeometry based on 7-geometry.py."""


class BaseGeometry:
    """The class BaseGeometry representing geometry object."""

    def area(self):
        """Calculates the area of geometry object.
        Raises:
            Exception: There is no logic"""

    def integer_validator(self, name, value):
        """Checks if the value is a valid integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

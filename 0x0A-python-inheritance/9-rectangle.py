#!/usr/bin/python3
"""This module writes class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py) based on 8-base_geometry.py."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The sub class representing an object inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Initialises Rectangle inherited from BaseGeometry."""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self) -> str:
        """Returns the string reprsentation of rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

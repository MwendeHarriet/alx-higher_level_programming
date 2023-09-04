#!/usr/bin/python3
"""This module defines a rectangle based on 2-rectangle.py."""


class Rectangle:
    """
    class Rectangle representing a rectangle.
    Attributes:
        width (int): Rectangle width.
        height (int): Rectangle height.
    """

    def __init__(self, width=0, height=0):
        """Initialises a class Rectangle with parameters width and height.
        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        Raises:
            ValueError: If width or height is below 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle' width.
        Args:
            value(int): Rectangle width.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is below 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the rectangle's height.
        Args:
            value(int): The rectangle height.
        Raises:
            TypeError: If height is not an int.
            ValueError: If height is below 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle's area.
        Returns:
            Rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the rectangle's perimeter.
        Returns:
            Rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """String representation of rectangle using '#'.
        Returns:
            str: Rectangle string representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for a in range(self.__height):
            rec_str += "#" * self.__width + "\n"
        return rec_str.strip()

#!/usr/bin/python3
"""This module writes class Square inheriting from Rectange(9-rectangle.py)
    based on 10-square.py."""


Rectangle = __import__('10-square').Square


class Square(Rectangle):
    """The sub class Square inheriting from Rectangle."""

    def __init__(self, size: int):
        super().integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """Calculates the area of the rectangle."""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

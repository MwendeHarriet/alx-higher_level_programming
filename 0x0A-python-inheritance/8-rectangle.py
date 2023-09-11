#!/usr/bin/python3
"""This module writes class Rectangle that inherits from 7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The sub-class Rectangle inherited from BaseGeometry."""

    def __init__(self, width: int, height: int):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

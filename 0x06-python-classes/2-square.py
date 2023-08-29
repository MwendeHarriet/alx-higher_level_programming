#!/usr/bin/python3
"""class Square module that defines a square"""


class Square:
    """the class square"""
    def __init__(self, size=0):
        """initialises a Square with its parameter size/
        the constructor/creates an instance of an object(class)
        Raises TypeError ValueError"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

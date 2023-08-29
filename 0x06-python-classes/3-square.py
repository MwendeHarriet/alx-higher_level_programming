#!/usr/bin/python3
"""class Square module that defines a square"""


class Square:
    """the class square/represents a square
    Attributes:
        __size (intt): Size of square.
    """

    def __init__(self, size=0):
        """
        Initialises a Square with its parameters size
        Args:
            size (int) the size of the square
        Raises:
            TypeError & ValueError-If size is not an integer &
            if size is less than 0 respectivrly
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square
        Returns:
            Current area of the square(int)
        """
        return self.__size ** 2

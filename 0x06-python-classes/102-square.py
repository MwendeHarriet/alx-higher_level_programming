#!/usr/bin/python3
"""class Square that module that defiens a square"""


class Square:
    """the class square/represents the square
    Attributes:
        __size (int) the Size of square.
    """

    def __init__(self, size=0):
        """
        Initialises a Square with parameters size
        Args:
            size (int) the size of the square
        Raises:
            TypeError & ValueError: If size is not an integer &
            if size is less than 0 respectively
        """
        self.size = size

    @property
    def size(self):
        """calculates the size of square
        Returns:
            size of the square(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets square size
        Args:
            value (int): the new square size
        Raises:
            TypeError & ValueError: If size is not an integer &
            if size is less than 0 respectively
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates the area of the square
        Returns:
             current square area(int)
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison to a Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison to a Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison to a Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison to a Square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison to a Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison to a Square"""
        return self.area() >= other.area()

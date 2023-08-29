#!/usr/bin/python3
"""class Square module that defines a square"""


class Square:
    """
    class square representing the square
    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """
        Initialises a Square with parameters size
        Args:
            size (int): size of the square
        Raises:
            TypeError & ValueError: If size is not an integer &
            If size is less than 0 respectively
        """
        self.size = size

    @property
    def size(self):
        """
        Calculates the size of square
        Returns:
            size of the square(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets square size
        Args:
            value (int):new square size
        Raises:
            TypeError & ValueError: If size is not an integer &
            if size is less than 0 respectively
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints square using '#'
        If size is 0 it prints an empty line
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)

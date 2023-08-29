#!/usr/bin/python3
"""class Square module that defines a square"""


class Square:
    """
    class square representing the square
    Attributes:
        __size (int): size of square
        __position (tuple): the square position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises Square with parameter size
        Args:
            size (int): size of the square
        Raises:
            TypeError & ValueError: If size is not an integer &
            if size is less than 0 respectively
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Calculates the square size
        Returns:
            size of the square(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the  square size
        Args:
            value (int): new square size
        Raises:
            TypeError & ValueError: If size is not an integer &
            if size is less than 0 respectively
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square
        Returns:
            tuple: the square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets square position
        Args:
            value (tuple): square position
        Raises:
            TypeError: If position is not a tuple of 2 +(positive) integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        i, j = value
        if not isinstance(i, int) or not isinstance(j, int) or i < 0 or j < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
             Current square area(int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square using '#'
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

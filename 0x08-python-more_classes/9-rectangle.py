#!/usr/bin/python3
"""This module defines a rectangle based on 8-rectangle.py."""


class Rectangle:
    """
    class Rectangle representing  a rectangle.
    Attributes:
        width (int): Rectangle width.
        height (int): Rectangle height.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises class Rectangle with parameters width and height.
        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        Raises:
            ValueError: If width or height is below 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """Creates a square instance of Rectangle.
        Args:
            cls (class): The class itself.
            size (int): The square size.
        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(size, size)

    @property
    def width(self):
        """Retrieves the  rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the  rectangle's width.
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
        """Calculates the  rectangle's area.
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

    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to return the rectangle with the bigger or equal area.
        Args:
            rect_1 (Rectangle): Rectangle instance.
            rect_2 (Rectangle): Second instance of Rectangle.
        Returns:
            Rectangle: Rectangle with the bigger or equal area.
        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """String reprepresentation of rectangle using '#'.
        Returns:
            str: Rectangle string representation.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for a in range(self.__height):
            rec_str += str(self.print_symbol) * self.__width + "\n"
        return rec_str.strip()

    def __repr__(self):
        """String representation of an object.
        Returns:
            str: Rectangle string representation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a goodbye message should instance be deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

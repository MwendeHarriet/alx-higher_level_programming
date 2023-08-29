#!/usr/bin/python3
import dis
import math


class MagicClass:
    """class that fefines MagicClass  that does/
    exactly as the bytecode in task 10
    It is calculating the area and circumference of a circle
    Attributes:
        __radius (float): the circle radius
    """

    def __init__(self, radius=0):
        """Initialises MagicClass with parameter radius
        Args:
            radius (float): circle radius
        Raises:
            TypeError: if the radius is not a number
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """Calculates the area of the circle
        Returns:
            float: the circle area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates circumferenece of a circle
        Returns:
            float: the circle circumference
        """
        return 2 * math.pi * self.__radius

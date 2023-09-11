#!/usr/bin/python3
"""This module writes class MyInt that inherits from int. MyInt is a little
    bit of a rebel because it has == and != operators inverted"""


class MyInt(int):
    """The sub class MyInt that inherits from int and inverting == and !=."""

    def __eq__(self, rando_num):
        """
        This function overrides the equality operator.
        Args:
            rando_num: the number to be compared
        """
        return super().__ne__(rando_num)

    def __ne__(self, rando_num):
        """
        This function overrides the inequality operator.
        Args:
            rando_num: the number to be compared
        """
        return super().__eq__(rando_num)

#!/usr/bin/python3
"""This  module inherits from list."""


class MyList(list):
    """class MyList class that inherits from list."""
    def print_sorted(self):
        """
        Prints the sorted list in ascending order.
        """
        print(sorted(self))

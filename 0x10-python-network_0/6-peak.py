#!/usr/bin/python3
"""This module finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """The find_peak function"""
    if list_of_integers == [] or len(list_of_integers) == 0:
        return None
    numbers = list_of_integers
    left = 0
    right = len(numbers) - 1
    while (left < right):
        middle = (left + right) // 2
        if numbers[middle] < numbers[middle+1]:
            left = middle + 1
        else:
            right = middle
    return numbers[left]

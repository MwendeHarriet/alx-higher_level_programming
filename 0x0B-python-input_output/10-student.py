#!/usr/bin/python3
"""This module defines class Student based on 9-student.py."""


class Student:
    """The class Student representing student."""

    def __init__(self, first_name, last_name, age):
        """Initialises a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictictionary representation
            of a student instance."""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            attr_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    attr_dict[i] = getattr(self, i)
            return attr_dict

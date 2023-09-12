#!/usr/bin/python3
"""This module defines class Student based on 10-student.py."""


class Student:
    """The class Student representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialises a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of
        a student instance."""
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

    def reload_from_json(self, json):
        """
        Substitutes all attributes of the student instance
        based on a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)

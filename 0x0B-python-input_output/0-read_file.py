#!/usr/bin/python3
"""This modeule reads files."""


def read_file(filename=""):
    """Reads and prints it's content."""

    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")

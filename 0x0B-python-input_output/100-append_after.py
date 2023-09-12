#!/usr/bin/python3
"""This module inserts a line of text to a file
    after each line containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Adds new text line after each line containing
    a specific string."""
    txt_lines = []
    with open(filename, 'r') as ifile:
        txt_lines = ifile.readlines()

    with open(filename, 'w') as ifile:
        for line in txt_lines:
            ifile.write(line)
            if search_string in line:
                ifile.write(new_string)

#!/usr/bin/python3
"""This script adds all arguments to a Python list and saves to a file."""


import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    args = load_from_json_file("add_item.json")
except Exception:
    args = []

for n in sys.argv[1:]:
    args.append(n)
save_to_json_file(dat, "add_item.json")

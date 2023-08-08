#!/usr/bin/python3
def remove_char_at(string, i):
    if i < 0 or i >= len(string):
        return string
    return string[:i] + string[i+1:]

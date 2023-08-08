#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if char == ' ':
            print(' ', end="")
        elif ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) & 223), end="")
        else:
            print(char, end="")
    print()

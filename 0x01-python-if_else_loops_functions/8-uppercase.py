#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if char == ' ':
            result += ' '
        elif ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) & 223)
        else:
            result += char
    print(result)

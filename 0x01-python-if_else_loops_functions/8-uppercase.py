#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        if ord('a') <= ord(alphabet) <= ord('z'):
            print(chr(ord(alphabet) - 32), end="")
        else:
            print(alphabet, end="")
    print()

#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        print("{:c}".format(ord(alphabet) & 223), end='')
    print()

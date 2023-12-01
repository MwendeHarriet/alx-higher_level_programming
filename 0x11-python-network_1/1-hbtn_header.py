#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the
    response"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.read()
        print(res.info().get('X-Request-Id'))

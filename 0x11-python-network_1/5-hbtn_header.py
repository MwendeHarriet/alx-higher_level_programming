#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header"""

if __name__ == "__main__":
    import requests
    import sys
    try:
        i = requests.get(sys.argv[1])
        print(i.headers['X-Request-Id'])
    except Exception:
        pass

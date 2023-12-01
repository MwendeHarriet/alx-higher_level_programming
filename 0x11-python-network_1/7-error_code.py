#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays
    the body of the response"""

if __name__ == "__main__":
    import requests
    import sys
    i = requests.get(sys.argv[1])
    if i.status_code == requests.codes.ok:
        print(i.text)
    else:
        print("Error code: {}".format(i.status_code))

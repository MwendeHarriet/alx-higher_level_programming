#!/usr/bin/python3
"""This script  script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8"""

if __name__ == "__main__":
    from urllib import request, parse, error
    import sys
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.URLError as e:
        print("Error code: {}".format(e.code))

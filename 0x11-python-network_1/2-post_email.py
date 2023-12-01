#!/usr/bin/python3
"""This script  takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of
    the response (decoded in utf-8)"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys
    email = sys.argv[2]
    data = {}
    data["email"] = email
    data = parse.urlencode(data).encode("utf-8")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

#!/usr/bin/python3
"""This script takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a parameter, and
    finally displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys
    email = sys.argv[2]
    data = {}
    data["email"] = email
    i = requests.post(sys.argv[1], data)
    print(i.text)

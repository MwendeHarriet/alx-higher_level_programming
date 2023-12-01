#!/usr/bin/python3
"""This script script that takes your GitHub credentials (username
    and password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth
    url = "https://api.github.com/user"
    i = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(i.json().get("id"))

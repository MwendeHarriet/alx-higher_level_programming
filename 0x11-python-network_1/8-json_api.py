#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a
    parameter"""

if __name__ == "__main__":
    import requests
    import sys
    data = {}
    try:
        data['q'] = sys.argv[1]
    except Exception:
        data['q'] = ""
    i = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        dictti = i.json()
        if len(dict_1) != 0:
            print("[{}] {}".format(dict_1["id"], dict_1["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")

#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value_url = {"email": sys.argv[2]}
    data_url = urllib.parse.urlencode(value_url).encode("ascii")

    req = urllib.request.Request(url, data_url)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

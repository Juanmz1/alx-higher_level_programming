#!/usr/bin/python3
"""Sends a POST request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value_url = {"email": sys.argv[2]}

    req = requests.post(url, value_url)
    print(req.text)

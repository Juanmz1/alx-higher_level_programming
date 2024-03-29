#!/usr/bin/python3
"""Displays the X-Request-Id header
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))

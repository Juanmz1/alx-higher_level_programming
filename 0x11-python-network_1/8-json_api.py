#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter
"""
import sys
import requests


if __name__ == "__main__":
    let_url = "" if len(sys.argv) == 1 else sys.argv[1]
    pay_url = {"q": let_url}

    req = requests.post("http://0.0.0.0:5000/search_user", data=pay_url)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Method that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    """
    url = argv
    with urllib.request.urlopen(url) as resp:
        headers = resp.info()
        print(headers['X-Request-Id'])

if __name__ == "__main__":
    main(argv[1])

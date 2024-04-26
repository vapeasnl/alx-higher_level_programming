#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


def main(argv):
    """
    Method that manage urllib.error.HTTPError exceptions
    """
    url = argv[1]
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))


if __name__ == "__main__":
    main(argv)

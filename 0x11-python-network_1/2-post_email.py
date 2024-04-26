#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        result = resp.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    main(argv)

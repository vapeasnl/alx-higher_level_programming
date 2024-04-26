#!/usr/bin/python3
"""Send a request to the url and print the response"""

from urllib import request, error
from sys import argv

def request_header_property(url: str) -> str:
    
    try:
        with request.urlopen(url) as rep:
            return rep.read().decode('utf-8')
    except error.HTTPError as err:
        return "Error code: {}".format(err.code)

if __name__ == "__main__":
    print(request_header_property(argv[1]))

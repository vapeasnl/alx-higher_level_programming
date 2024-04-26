#!/usr/bin/python3
"""displays value of the X-Request-Id in response"""

from urllib import request, error
from sys import argv

def request_header_property(url: str) -> str:
    
    try:
        with request.urlopen(url) as rep:
            return rep.info()['X-Request-Id']
    except error.URLError as er:
        return er.reason

if __name__ == "__main__":
    print(request_header_property(argv[1]))

#!/usr/bin/python3

"""
send a GET request to a the url provided
"""

from requests import get
from sys import argv

def get_alx_intranet(url):
    
    if url:
        try:
            return get(url).headers.get('X-Request-Id')
        except Exception as exc:
            return exc

if __name__ == "__main__":
    print(get_alx_intranet(argv[1]))

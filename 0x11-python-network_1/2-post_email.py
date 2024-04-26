#!/usr/bin/python3
"""send an email to the url and print the response"""

from urllib import request, error, parse
from sys import argv

def send_email_to_url(url: str, email: str) -> str:
    data = {}
    data['email'] = email
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, data, method="POST")
    try:
        with request.urlopen(req) as rep:
            return rep.read().decode("utf-8")
    except error.URLError as err:
        return err.reason

if __name__ == "__main__":
    print(send_email_to_url(argv[1], argv[2]))


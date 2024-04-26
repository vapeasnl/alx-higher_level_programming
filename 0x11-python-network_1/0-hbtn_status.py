#!/usr/bin/python3
"""get https://alx-intranet.hbtn.io/status"""
from urllib import request, error

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with request.urlopen(url) as rep:
            rep = rep.read()
            print("Body response:")
            print("\t- type: {}".format(type(rep)))
            print("\t- content: {}".format(rep))
            print("\t- utf8 content: {}".format(rep.decode('utf-8')))
    except error.URLError:
        print("Cannot connect to https://alx-intranet.hbtn.io/status")

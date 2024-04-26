#!/usr/bin/python3

"""
get https://alx-intranet.hbtn.io/status
"""

from requests import get

def get_alx_intranet(url='https://alx-intranet.hbtn.io/status'):
    
    stat = get(url)
    print("Body response:")
    print("\t- type: {}".format(str(stat).__class__))
    print("\t- content: {}".format(stat.text))

if __name__ == "__main__":
    get_alx_intranet()

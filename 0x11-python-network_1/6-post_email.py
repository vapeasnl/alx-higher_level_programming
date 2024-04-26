#!/usr/bin/python3
"""send an email to the url and print the response"""

from requests import post
from sys import argv

def send_email_to_url(url: str, email: str) -> str:
    
    data = {}
    data['email'] = email
    try:
        return (post(url, data=data).text)
    except Exception as e:
        return e

if __name__ == "__main__":
    print(send_email_to_url(argv[1], argv[2]))

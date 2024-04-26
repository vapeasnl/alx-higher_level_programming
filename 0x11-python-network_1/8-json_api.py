#!/usr/bin/python3
"""
Send a POST request to localhost:5000/search_user
"""

from requests import post
from sys import argv

def send_query(query_string: str) -> str:
    
    server = "http://0.0.0.0:5000/search_user"
    resp = post(server, data={'q': query_string}).text
    try:
        resp_json = eval(resp)
        if len(resp_json) != 0:
            return "[{}] {}".format(resp_json.get('id'), resp_json.get('name'))
        return "No result"
    except Exception as e:
        return "Not a valid JSON"

if __name__ == "__main__":
    if len(argv) >= 2:
        print(send_query(argv[1]))
    else:
        print(send_query(""))

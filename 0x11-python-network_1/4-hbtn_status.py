#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print('Body response:\n\
\t- type: {}\n\
\t- content: {}'.format(type(text), text))

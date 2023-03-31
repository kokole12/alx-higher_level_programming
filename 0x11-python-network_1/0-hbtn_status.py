#!/usr/bin/python3
import urllid.request
""" Python script to sent request to a given url"""


if __name__ == "__main__":
    req = urllid.request.Request('https://alx-intranet.hbtn.io/status')
    with urllid.request.urlopen(req) as response:
        status = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(status)))
        print('\t- content: {}'.format(status))
        print('\t- utf8 content: {}'.format(status.decode('utf-8')))

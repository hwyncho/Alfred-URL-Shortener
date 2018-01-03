#-*- coding: utf-8 -*-
#!/usr/bin/python

"""
Created by 조휘연 on 2018. 01. 02.
Copyright © 2018년 조휘연. All rights reserved.
==================================================
GitHub : https://github.com/hwyncho/Alfred-URL-Shortener/
e-mail : hwyn.cho@gmail.com
"""

import json
import sys

try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen


def url_shorten(long_url):
    """
    Shorten URL with Google API.

    :param long_url: str
        Long URL

    :return short_url: str
        Short URL
    """
    try:
        api_key = 'AIzaSyCnj0Ff5xrX-QFX4lrXLRrqzFAU-nfSmYk'

        url = 'https://www.googleapis.com/urlshortener/v1/url?key={0}'.format(
            api_key)

        data = json.dumps({'longUrl': long_url}).encode('utf-8')
        headers = {'Content-Type': 'application/json',
                   'Content-Length': str(len(data))}

        req = Request(url=url, headers=headers)
        res = urlopen(url=req, data=data).read().decode('utf-8')

        short_url = json.loads(res)['id']

        return short_url
    except Exception as err:
        return str(err)


if __name__ == '__main__':
    q = "{query}"
    sys.stdout.write(url_shorten(q))

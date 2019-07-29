#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    py3practice.httprequest
    ~~~~~~~~~~~~~~~~~~~
    Send some httprequest for demo

    :copyright: © 2018 by zenanswer.
    :license: MIT, see LICENSE for more details.
"""

import requests
import json
from functools import wraps


def log_func(function):
    @wraps(function)
    def function_show_name(*args, **kwargs):
        print('=== %s === %s %s' % (function.__name__, args, kwargs))
        return function(*args, **kwargs)
    return function_show_name


@log_func
def requestQQ(allow_redirects=True):
    r = requests.get('http://www.qq.com', allow_redirects=allow_redirects)
    print(r.status_code, r.reason, len(r.text))
    print(r.headers, r.history)
    return r


@log_func
def askWeather():
    r = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
    bj_weather = json.loads(r.content.decode("utf-8"))['weatherinfo']
    print(
        '%s 温度：%s 湿度：%s' %
        (bj_weather['city'], bj_weather['temp'], bj_weather['SD']))


@log_func
def getTangPoetry(page=1, count=1):
    r = requests.get('https://api.apiopen.top/getTangPoetry',
                     params={'page': page, 'count': count})
    print(r.url)
    poetries = json.loads(r.content.decode("utf-8"))['result']
    for poetry in poetries:
        print(poetry['title'])
        print(poetry['content'].replace('|', '\r\n'))


@log_func
def postCreateUser():
    # https://reqres.in/
    actor = {
        "name": "paul rudd",
        "movies": ["I Love You Man", "Role Models"]
    }
    r = requests.post('https://reqres.in/api/users', data=json.dumps(actor))
    print(r.status_code, r.reason, len(r.text))
    actor_id = json.loads(r.content.decode("utf-8"))['id']
    print(actor_id)


@log_func
def postEchoWithHeader():
    # https://docs.postman-echo.com/
    actor = {
        "name": "paul rudd",
        "movies": ["I Love You Man", "Role Models"]
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post('https://postman-echo.com/post',
                      data=json.dumps(actor),
                      headers=headers)
    print(r.status_code, r.reason)
    print(json.dumps(
            json.loads(r.content.decode("utf-8")),
            indent=2,
            sort_keys=True))


if __name__ == '__main__':
    requestQQ()
    requestQQ(allow_redirects=False)
    askWeather()
    # getTangPoetry(1, 3)
    # getTangPoetry(2, 3)
    postCreateUser()
    postEchoWithHeader()

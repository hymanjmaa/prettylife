# -*- coding: utf-8 -*-
import requests
import json

__author__ = 'Hyman'
__time__ = '2017-06-24 1:10'

global s
s = requests.session()


def talk(content, userid):
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": "ec047e7c35f540dab4b34dfa06fa9a32", "info": content, "userid": userid}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    code = j['code']
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text'] + j['url']
    elif code == 302000:
        recontent = j['text'] + j['list'][0]['info'] + j['list'][0]['detailurl']
    elif code == 308000:
        recontent = j['text'] + j['list'][0]['info'] + j['list'][0]['detailurl']
    else:
        recontent = '小慢还没学会怎么回复这句话'
    return recontent


if __name__ == "__main__":
    print talk("你好")
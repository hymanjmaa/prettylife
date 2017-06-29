# -*- coding: utf-8 -*-
import urllib
import time
import json
__author__ = 'Hyman'
__time__ = '2017-06-24 18:46'

# 获取accessToken

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0

    def __real_get_access_token(self):
        appId = "wxb3b0feb69a3a6dc6"
        appSecret = "59cc100110e6a844375b2ec670005af3"

        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                   "client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())

        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']

    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken

    def run(self):
        while (True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()


def main():
    pass


if __name__ == "__main__":
    main()

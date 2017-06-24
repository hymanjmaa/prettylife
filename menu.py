# -*- coding: utf-8 -*-
import urllib
from basic import Basic
__author__ = 'Hyman'
__time__ = '2017-06-24 19:46'


class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()


def createMenu():
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "马小骏",
                "key":  "hymanj"
            },
            {
                "name": "PrettyLife",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "最近",
                        "url": "http://mp.weixin.qq.com/s/BFriNhZ9ISsN_Wsws92tEg"
                    },
                    {
                        "type": "view",
                        "name": "历史",
                        "url": "http://mp.weixin.qq.com/mp/homepage?__biz=MjM5NTQ5MDA0MQ==&hid=1&sn=c6a97850b5354f9ae48d8933214a166c#wechat_redirect"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "待定",
                "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
            }
        ]
    }
    """
    accessToken = Basic().get_access_token()
    # myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)


if __name__ == "__main__":
    createMenu()

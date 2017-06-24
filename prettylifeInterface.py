# -*- coding: utf-8 -*-
import hashlib
import os

import web

import weixin.receive
import weixin.reply
import weixin.talk_tuling_api


class PrettyLifeInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        try:
            # 获取输入参数
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            # 自己的token
            token = "prettylifetimehymanjma"  # 这里改写你在微信公众平台里输入的token
            # 字典序排序
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            # sha1加密算法

            # 如果是来自微信的请求，则回复echostr
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            # print "Handle Post webdata is ", webData  # 后台打日志
            recMsg = weixin.receive.parse_xml(webData)
            if isinstance(recMsg, weixin.receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                userid = hashlib.md5(fromUser).hexdigest()
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    try:
                        msg = weixin.talk_tuling_api.talk(content, userid)
                        replyMsg = weixin.reply.TextMsg(toUser, fromUser, msg)
                    except:
                        replyMsg = weixin.reply.TextMsg(toUser, fromUser, "没听懂咋整啊")
                        # replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = weixin.reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                if recMsg.MsgType == 'voice':
                    content = recMsg.Recognition
                    try:
                        msg = weixin.talk_tuling_api.talk(content, userid)
                        replyMsg = weixin.reply.TextMsg(toUser, fromUser, msg)
                    except:
                        replyMsg = weixin.reply.TextMsg(toUser, fromUser, '这货还不够聪明，换句话聊天吧')
                    return replyMsg.send()
                else:
                    replyMsg = weixin.reply.TextMsg(toUser, fromUser, '这货还处理不了这种类型的聊天')
                    return replyMsg.send()
                    # return reply.Msg().send()
            else:
                replyMsg = weixin.reply.TextMsg(recMsg.FromUserName, recMsg.ToUserName, '有bug你懂的')
                return replyMsg.send()
                # print "暂且不处理"
                # return "success"
        except Exception, Argment:
            return Argment


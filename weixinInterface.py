# -*- coding: utf-8 -*-
import hashlib
import web
import reply
import receive


class WeixinInterface:
    # def __init__(self):
    #     self.app_root = os.path.dirname(__file__)
    #     self.templates_root = os.path.join(self.app_root, 'templates')
    #     self.render = web.template.render(self.templates_root)

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
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
        # str_xml = web.data()  # 获得post来的数据
        # xml = etree.fromstring(str_xml)  # 进行XML解析
        # msgType = xml.find("MsgType").text
        # fromUser = xml.find("FromUserName").text
        # toUser = xml.find("ToUserName").text
        # if msgType == 'text':
        #     content = xml.find("Content").text
        #     return self.render.reply_text(fromUser, toUser, int(time.time()), "test")
        # elif msgType == 'image':
        #     pass
        # else:
        #     pass

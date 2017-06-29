# -*- coding: utf-8 -*-
import hashlib
import os
import web
import receive
import reply
import talk_tuling_api


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
            webData = web.data()  # Tencent服务器向SAE推送数据
            # print "Handle Post webdata is ", webData  # 后台打日志
            recMsg = receive.parse_xml(webData)  # 解析xml数据

            # 事件消息处理
            if recMsg.MsgType == 'event':
                event = recMsg.Event
                if event == 'subscribe':  # 关注事件
                    welcome = '我是马小骏，已经3岁啦☺\n' \
                              '智能系数不高，聊天解闷还凑合吧\n' \
                              '<a href="http://mp.weixin.qq.com/mp/homepage?__biz=MjM5NTQ5MDA0MQ==&hid=1&sn=c6a97850b5354f9ae48d8933214a166c#wechat_redirect">☞我的历史☜</a>\n' \
                              '我默认是机器人模式，不信你试试？\n' \
                              '我还在学习中，学无止境嘛 '
                    replyMsg = reply.TextMsg(recMsg.FromUserName, recMsg.ToUserName, welcome)
                    return replyMsg.send()
                elif event == 'unsubscribe':  # 取消关注事件
                    return ""
                else:
                    return ""

            # 判断是否为可回复消息
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName  # 获取消息发送方账号
                fromUser = recMsg.ToUserName  # 获取开发者账号
                # 将发送方账号md5加密，传入图灵机器人接口便于机器人识别上下文
                userid = hashlib.md5(fromUser).hexdigest()

                if recMsg.MsgType == 'text':  # 文本消息处理
                    content = recMsg.Content  # 去除用户发送文本
                    try:
                        msg = talk_tuling_api.talk(content, userid)  # 获取图灵机器人回复
                        replyMsg = reply.TextMsg(toUser, fromUser, msg)
                    except Exception:
                        replyMsg = reply.TextMsg(toUser, fromUser, "没听懂咋整啊")
                    return replyMsg.send()

                if recMsg.MsgType == 'image':  # 图片消息处理
                    mediaId = recMsg.MediaId  # 取出用户发送图片素材id
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()

                if recMsg.MsgType == 'voice':  # 语音消息处理
                    content = recMsg.Recognition  # 取出语音识别后文本
                    # mediaId = recMsg.MediaId  # 获取语音消息id
                    try:
                        msg = talk_tuling_api.talk(content, userid)  # 获取图灵机器人回复
                        replyMsg = reply.TextMsg(toUser, fromUser, msg)
                        # replyMsg = reply.VoiceMsg(toUser, fromUser, mediaId)  # 原样回复用户发送的语音
                    except Exception:
                        replyMsg = reply.TextMsg(toUser, fromUser, '这货还不够聪明，换句话聊天吧')
                    return replyMsg.send()

                if recMsg.MsgType == 'video':  # 视频消息处理
                    mediaId = recMsg.MediaId  # 取出用户发送视频素材id
                    # replyMsg = reply.VideoMsg(toUser, fromUser, mediaId)
                    replyMsg = reply.TextMsg(toUser, fromUser, "你...你竟然给我发小电影!")
                    return replyMsg.send()

                if recMsg.MsgType == 'location':  # 地理位置消息处理
                    Location_X = recMsg.Location_X
                    Location_Y = recMsg.Location_Y
                    Scale = recMsg.Scale
                    Label = recMsg.Label
                    loc = '您的坐标(x_'+Location_X+')(y_'+Location_Y+'),位于'+Label
                    replyMsg = reply.TextMsg(toUser, fromUser, loc)
                    return replyMsg.send()

                if recMsg.MsgType == 'link':
                    Title = recMsg.Title
                    Description = recMsg.Description
                    Url = recMsg.Url
                    msg = Title+Description+Url
                    replyMsg = reply.TextMsg(toUser, fromUser, msg)
                    return replyMsg.send()

                else:
                    replyMsg = reply.TextMsg(toUser, fromUser, '这货还处理不了这种类型的聊天')
                    return replyMsg.send()
                    # return reply.Msg().send()

            else:
                replyMsg = reply.TextMsg(recMsg.FromUserName, recMsg.ToUserName, '服务器有点累，等会儿再来')
                return replyMsg.send()
                # print "暂且不处理"
                # return "success"

        except Exception, Argment:
            return Argment


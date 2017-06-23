# coding: UTF-8
import os
import sae
import web

from weixinInterface import WeixinInterface

urls = (
'/weixin','WeixinInterface'
)


app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

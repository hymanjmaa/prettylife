# coding: UTF-8
import os
import sae
import web
sae.add_vendor_dir('vendor')
from prettylifeInterface import PrettyLifeInterface
from menu import main

urls = (
'/weixin','PrettyLifeInterface'，
'/weixin','main'
)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

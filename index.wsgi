# coding: UTF-8
import os
import sae
import web
sae.add_vendor_dir('vendor')
from prettylifeInterface import PrettyLifeInterface

urls = (
'/weixin','PrettyLifeInterface'
)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

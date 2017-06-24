# coding: UTF-8
import os
import sae
import web
sae.add_vendor_dir('vendor')
from prettylifeInterface import PrettyLifeInterface

import sae from sae.ext.shell
import ShellMiddleware
def app(environ, start_response):
    status = ‘200 OK’
    response_headers = [(‘Content-type’, ‘text/plain’)]
    start_response(status, response_headers)
    return [“Hello, world!”]
application = sae.create_wsgi_app(ShellMiddleware(app))

urls = (
'/weixin','PrettyLifeInterface'
)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

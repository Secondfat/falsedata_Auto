# -*- coding: utf-8 -*-
import logging
import socket
from ddt import ddt, data, unpack

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import sys
import urllib
from tornado.web import HTTPError, asynchronous
from tornado.httpclient import HTTPRequest
from tornado.options import define, options

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

try:
    from tornado.curl_httpclient import CurlAsyncHTTPClient as AsyncHTTPClient
except ImportError:
    from tornado.simple_httpclient import SimpleAsyncHTTPClient as AsyncHTTPClient
 
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, type=bool)
 
class ProxyHandler(tornado.web.RequestHandler):
    SUPPORTED_METHODS = ("CONNECT", "GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS")
    @tornado.web.asynchronous
    def connect(self):
        '''
        对于HTTPS连接，代理应当作为TCP中继
        '''
        def req_close(data):
            if conn_stream.closed():
                return
            else:
                conn_stream.write(data)

        def write_to_server(data):
            conn_stream.write(data)

        def proxy_close(data):
            if req_stream.closed():
                return
            else:
                req_stream.close(data)

        def write_to_client(data):
            req_stream.write(data)

        def on_connect():
            print "on connect"
            '''
            创建TCP中继的回调
            '''
            req_stream.read_until_close(req_close, write_to_server)
            conn_stream.read_until_close(proxy_close, write_to_client)
            req_stream.write(b'HTTP/1.0 200 Connection established\r\n\r\n')
    
        print 'Starting Conntect to %s' %  self.request.uri
        # 获取request的socket
        req_stream = self.request.connection.stream
        print req_stream

        # 找到主机端口，一般为443
        host, port = (None, 443)
        netloc = self.request.uri.split(':')
        if len(netloc) == 2:
            host, port = netloc
        elif len(netloc) == 1:
            host = netloc[0]

        # 创建iostream
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        conn_stream = tornado.iostream.IOStream(s)
        conn_stream.connect((host, 443), on_connect)

    #print "testest"
    @asynchronous
    def get(self):
        # enable API GET request when debugging
        if options.debug:
            return self.post()
        else:
            raise HTTPError(405)

    @asynchronous
    def post(self):
        url = self.request.uri

        # update host to destination host
        headers = dict(self.request.headers)
 
        try:
            AsyncHTTPClient().fetch(
                HTTPRequest(url=url,
                            method="POST",
                            body=self.request.body,
                            headers=headers,
                            follow_redirects=False),
                self._on_proxy)
        except tornado.httpclient.HTTPError, x:
            if hasattr(x, "response") and x.response:
                self._on_proxy(x.response)
            else:
                logging.error("Tornado signalled HTTPError %s", x)
 
    def _on_proxy(self, response):
        if response.error and not isinstance(response.error, tornado.httpclient.HTTPError):
            raise HTTPError(500)
        else:
            for header in ("Date", "Cache-Control", "Server", "Content-Type", "Location"):
                v = response.headers.get(header)
        #print v
                if v:
                    self.set_header(header, v)
            if response.body:
                self.write(response.body)
                self.finish()
        #self.render("template.html", title="My title", items=["item1","item2"])
		#print response.body
		

def writeDataToFile(filename,content):
    file=open("data/"+ urllib.quote(filename), 'w+')
    file.write(content)
    file.close()
    return;

def readDataFromFile(filename):
    file=open("data/"+ urllib.quote(filename),'r')
    content=file.read()
    file.close()
    return content;

def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r".*", ProxyHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()

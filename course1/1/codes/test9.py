#coding=utf-8

import tornado.web
import tornado.ioloop

class CookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_cookie('uname','zhangsan',expires_days=3)

        self.set_secure_cookie('hello','lisi')

class GetCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # uname = self.get_cookie('uname')

        uname = self.get_secure_cookie('hello')
        self.write(uname)

settings = {
    'cookie_secret':'abcdefg'
}


app = tornado.web.Application([
    (r'^/$',CookieHandler),
    (r'^/getCookie/$',GetCookieHandler)
],**settings)


app.listen(8000)

tornado.ioloop.IOLoop.instance().start()
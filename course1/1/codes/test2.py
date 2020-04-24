# coding=utf-8


import tornado.ioloop
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/login.html')


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')

        uname = self.get_query_argument('uname')

        print(uname, pwd)
        self.write(uname + ',' + pwd)

    def post(self, *args, **kwargs):
        # uname = self.get_argument('uname')

        uname = self.get_body_argument('uname')
        print(uname)
        self.write(uname)


app = tornado.web.Application([
    (r'^/$', IndexHandler),
    (r'^/login/$', LoginHandler)
])

app.listen(8888)

# tornado.ioloop.IOLoop.current().start()
tornado.ioloop.IOLoop.instance().start()

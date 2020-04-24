#coding=utf-8


import tornado.web
import tornado.ioloop
from tornado.web import RedirectHandler
from tornado.routing import URLSpec


class IndexHandler(tornado.web.RequestHandler):



    def get(self, *args, **kwargs):
        #302重定向
        # self.redirect('https://www.baidu.com')

        self.set_status(301)
        self.set_header('Location','https://www.jd.com')





class ReverseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect(self.reverse_url('index'))



app = tornado.web.Application([
    (r'^/$',IndexHandler),
    (r'^/red/$',RedirectHandler,{'url':'https://www.taobao.com'}),
    URLSpec(r'^/fdsafdslajjflds$',IndexHandler,name='index'),
    (r'^/reverse/$', ReverseHandler),

])

app.listen(8000)


tornado.ioloop.IOLoop.instance().start()
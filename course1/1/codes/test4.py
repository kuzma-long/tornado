# coding=utf-8


import tornado.ioloop
import tornado.web


class GetRequestInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request)
        print(self.request.protocol)
        print(self.request.host)
        print(type(self.request.headers))
        print(self.request.headers['User-Agent'])


ugs = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36']


class StuHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 1.获取请求头中user-agent的值
        ua = self.request.headers['User-Agent']

        # 2.判断
        if ua not in ugs:
            self.send_error(403)

        else:
            self.write('hello XXX')


app = tornado.web.Application([
    (r'^/$', GetRequestInfo),
    (r'^/stu/$', StuHandler)
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()

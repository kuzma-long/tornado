# coding=utf-8

import tornado.ioloop
import tornado.web


# 创建处理类
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello tornado!')


# 创建Application对象
app = tornado.web.Application([
    (r'/', IndexHandler)
])

# 绑定监听端口号
app.listen(8888)

# 启动监听
tornado.ioloop.IOLoop.instance().start()

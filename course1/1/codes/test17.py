#coding=utf-8

from tornado.web import RequestHandler,Application,StaticFileHandler
from tornado.ioloop import IOLoop
import os

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('readImg.html')



app = Application([
    (r'^/$',IndexHandler),
    # (r"/static/(.*)", StaticFileHandler, {"path": os.path.join(os.getcwd(),'static','images')}),
],template_path=os.path.join(os.getcwd(),'templates'),static_path=os.path.join(os.getcwd(),'static','images'))


app.listen(8000)


IOLoop.instance().start()
#coding=utf-8

from tornado.web import RequestHandler,Application
from tornado.ioloop import IOLoop
import os
class Person(object):
    def __init__(self,sname,spwd):
        self.sname = sname
        self.spwd = spwd


def reverse(obj):
    if isinstance(obj,list):
        obj.reverse()
    return obj

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        person = Person('lisi','123')

        clist = ['c1','c2','c3']

        mdict = {'k1':'v1','k2':'v2'}

        str = '<script>window.location.href="https://www.baidu.com";</script>'

        self.render('index01.html',uname='zhangsan',person=person,clist=clist,mdict=mdict,r=reverse,str=str)


app = Application([
    (r'^/$',IndexHandler)
],template_path=os.path.join(os.getcwd(),'templates'))

app.listen(8000)

IOLoop.instance().start()
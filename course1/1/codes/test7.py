#coding=utf-8


class BaseHandler(object):
    def initialize(self):
        print '初始化方法'


    def get(self):
        raise Exception('405')


    def post(self):
        raise Exception('405')

    def on_finish(self):
        print '请求结束'

class IndexHandler(BaseHandler):
    def initialize(self,conn):
        print conn
        print '调用子类的初始化方法'

    def get(self):
        print '调用子类的GET方法'


if __name__ == '__main__':
    #配置路由
    urlpatterns = [(r'/',IndexHandler,{'conn':'123'})]
    #设置请求地址
    action = '/'

    #设置用户的请求方式
    method = 'post'

    for url in urlpatterns:
        p,c,d = url
        if action == p:
            index = c()
            index.initialize(d)
            getattr(index,method)()
            index.on_finish()







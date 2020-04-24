#coding=utf-8

import tornado.web
import tornado.ioloop
import MySQLdb



class LoginHandler(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def prepare(self):
        #判断当前请求方式
        if self.request.method == 'POST':
            #获取请求参数
            self.uname = self.get_argument('uname')
            self.pwd = self.get_argument('pwd')




    def get(self, *args, **kwargs):
        self.render('templates/login.html')

    def post(self, *args, **kwargs):
        1/0
        cursor = self.conn.cursor()
        cursor.execute('select * from t_auser where uname="%s" and pwd="%s"'%(self.uname,self.pwd))
        user = cursor.fetchone()

        if user:
            self.write(u'登录成功！')

        else:
            self.write(u'登录失败！')

    def write_error(self, status_code, **kwargs):
        self.render('templates/error.html')

    def set_default_headers(self):
        self.set_header('Server','SXTServer/1.0')



settings={'debug':True}
dbconfig={
    'host':'127.0.0.1',
    'user':'root',
    'passwd':'123456',
    'db':'tornaod20180830',
    'port':3306

}


app = tornado.web.Application([
    (r'^/login/$',LoginHandler,{'conn':MySQLdb.connect(**dbconfig)})
],**settings)


app.listen(8000)

tornado.ioloop.IOLoop.instance().start()
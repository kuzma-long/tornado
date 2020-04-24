#coding=utf-8


import tornado.web
import tornado.ioloop
import MySQLdb

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.render('templates/error.html')

    def set_default_headers(self):
        self.set_header('Server','SXTServer/1.0')

    def uuid(self):
        import uuid
        return uuid.uuid4().get_hex()


class BaseDBHandler(BaseHandler):
    def initialize(self,conn):
        self.conn = conn

    def fetchone(self,sql):
       cursor = self.conn.cursor()
       cursor.execute(sql)
       data = cursor.fetchone()
       cursor.close()
       return data


    def updateToken(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()


class LoginHandler(BaseDBHandler):
    def prepare(self):
        if self.request.method == 'POST':
            self.uname = self.get_argument('uname')
            self.pwd = self.get_argument('pwd')


    def get(self, *args, **kwargs):
        self.render('templates/login.html')


    def post(self, *args, **kwargs):
        user = self.fetchone('select * from t_buser where uname="%s" and pwd="%s"'%(self.uname,self.pwd))

        print user

        #判断是否登录成功
        if user:
            uid = self.uuid()
            self.updateToken('update t_buser set token="%s" where userid="%s"'%(uid,user[0]))

            #将uid保存到cookie中
            if not self.get_cookie('c_cookie'):
                self.set_cookie('c_cookie',uid)

            self.redirect('/center/')
        else:
            self.get()


class CenterHandler(BaseDBHandler):
    def prepare(self):
        #从cookie中获取之前保存的uid
        uid = self.get_cookie('c_cookie')
        #查询数据库的sql
        self.sql = 'select uname from t_buser where token="%s"'%uid


    def get(self, *args, **kwargs):
        user = self.fetchone(self.sql)
        if user:
            self.write(u'欢迎-%s-登录成功！'%user[0])
        else:
            self.write(u'只能在同一个浏览器中进行访问！')



dbconfig={
    'host':'127.0.0.1',
    'user':'root',
    'passwd':'123456',
    'db':'tornaod20180830',
    'port':3306

}



app = tornado.web.Application([
    (r'^/login/$',LoginHandler,{'conn':MySQLdb.connect(**dbconfig)}),
    (r'^/center/$',CenterHandler,{'conn':MySQLdb.connect(**dbconfig)})
])


app.listen(8000)

tornado.ioloop.IOLoop.instance().start()

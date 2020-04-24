#coding=utf-8

from tornado.template import Loader
import os


if __name__ == '__main__':
    #创建Loader对象
    loader = Loader(os.path.join(os.getcwd(),'templates'))

    #获取一个模板对象
    t = loader.load('index.html')
    content = t.generate(uname='明天放假咯')
    print content

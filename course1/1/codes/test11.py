#coding=utf-8

from tornado.template import Template
import os


if __name__ == '__main__':
    with open(os.path.join(os.getcwd(),'templates','index.html'),'rb') as fr:
        content = fr.read()

    t = Template(content)
    content = t.generate(uname='douyin')
    print content

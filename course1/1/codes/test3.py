# coding=utf-8

import tornado.ioloop
import tornado.web


class UploadHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/upload.html')

    def post(self, *args, **kwargs):
        # 获取请求参数
        # [{'body': '\0\x00IEND\xaeB`\x82', 'content_type': u'image/png', 'filename': u'1.png'}]
        img1 = self.request.files['img1']

        # 遍历img1
        for img in img1:
            body = img.get('body', '')
            content_type = img.get('content_type', '')
            filename = img.get('filename', '')

        # 将图片存放至files目录中
        import os
        dir = os.path.join(os.getcwd(), 'files', filename)

        with open(dir, 'wb') as fw:
            fw.write(body)

        # 将图片显示到浏览器页面中
        # 设置响应头信息
        self.set_header('Content-Type', content_type)
        self.write(body)


app = tornado.web.Application([
    (r'/upload/', UploadHandler)
])

app.listen(8888)

tornado.ioloop.IOLoop.instance().start()

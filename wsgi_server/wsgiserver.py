#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8000，处理class是RequestHandler，会调用__call__函数:
from wsgi_server.reqhandler import RequestHandler

if __name__ == '__main__':
    httpd = make_server('', 8000, RequestHandler())
    print("Serving HTTP on port 8000...")
    # 开始监听HTTP请求:
    httpd.serve_forever()

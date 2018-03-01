#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import socket

HOST, PORT = 'localhost', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print("Serving HTTP on port ", HOST, PORT)
print("host: %s port: %d" % (HOST, PORT))
print("host: {0}, port: {1}".format(HOST, PORT))
print("host: {host}, port: {port}".format(host=HOST, port=PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

#    http_response = """
#    HTTP/1.1 200 OK
#
#    Hello, World!
#    """

#    http_response = """
#    Hello, World!
#    """

    # \n 千万不要少了，因为前面的 server 是按行读取的
    http_response = "hello\n"

    # client_connection.sendall("hello".encode('utf-8'))
    # client_connection.send("HTTP/1.1 200 OK hello".encode('utf-8'))
    # client_connection.send("/HTTP/1.1 200 OK hello".encode('utf-8'))
    # client_connection.send("/aa HTTP/1.1 200 OK hello".encode('utf-8'))
    # client_connection.send("/hello".encode('utf-8'))

    client_connection.sendall(http_response.encode('utf-8'))
    # client_connection.sendall(http_response.encode('utf-8'))
    client_connection.close()
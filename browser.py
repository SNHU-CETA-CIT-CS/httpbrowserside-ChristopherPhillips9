#!/usr/bin/env python
__author__ = "Arana Fireheart"
import socket

webSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
webSocket.connect(("data.pr4e.org", 80))
command = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
webSocket.send(command)

data = ' '
while len(data) > 0:
    data = webSocket.recv(512)
    print(data.decode(), end='')

webSocket.close()
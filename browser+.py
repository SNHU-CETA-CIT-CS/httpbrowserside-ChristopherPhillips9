#!/usr/bin/env python
__author__ = "Arana Fireheart"
import socket

PORTNUMBER = 80
URL = "data.pr4e.org"
PAGE = "page1.htm"

headers = [f"Host: {URL}\r\n",
             "Accept-Language: en-us\r\n",
             "Accept-Encoding: gzip, deflate\r\n",
             "Connection: Keep-Alive"
           ]

headerData = "".join(headers)
httpRequest = f"GET http://{URL}/{PAGE} \r\n"
commandData = f"{httpRequest}{headerData}"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as webSocket:
    try:
        webSocket.connect(("data.pr4e.org", PORTNUMBER))
        command = commandData.encode()
        webSocket.send(command)
    except socket.error as exc:
        print(f"A socket error has occurred : {exc}")

    data = ' '
    while len(data) > 0:
        data = webSocket.recv(512)
        print(data.decode(), end='')
pass

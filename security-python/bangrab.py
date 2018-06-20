#!/usr/bin/python
import socket
#import the socket module
socket.setdefaulttimeout(2)
s=socket.socket()
s.connect(("<ip-address>", <port-number>))
ans = s.recv(1024)
print ans


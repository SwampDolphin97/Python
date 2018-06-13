#!/usr/bin/python
import socket
def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip, port))
        banner=s.recv(1024)
        return banner
    except:
        return
    def main():
        ip1='<IP-ADDRESS>'
        ip2='<IP-ADDRESS>'
        port=21

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
banner1 = retbanner(ip1, port)
if banner1:
    print '[+]' + ip1 + ':' + banner1
banner2 = retbanner(ip2, port)
if banner2:
    print '[+]' + ip2 + ':' + banner2
if __name__=='__main__':
    main()


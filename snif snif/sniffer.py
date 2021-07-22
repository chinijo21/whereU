import os
import socket

#host to listen
HOST = '192.168.56.1'

def init():
    #bin to public interface and check for windows
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP


if __name__ == '__main__':
    init()  
            
import os
import socket

#host to listen
HOST = '192.168.1.106'

def init():
    #bin to public interface and check for windows
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    #def HOST IP and construct socket object w neccesary params
    snifit = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    snifit.bind((HOST, 0))
    
    #socket that includes IP Heads of captured packages
    snifit.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    #Windows? set network card to promiscous by sending IOCTL
    if os.name == 'nt':
        snifit.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    #read a packet
    print(snifit.recvfrom(65565))
    
    #WIndows? turn off prom mode
    if os.name == 'nt':
        snifit.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    
    

if __name__ == '__main__':
    init()  
            
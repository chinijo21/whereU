import os
import socket
import struct
import sys
import ipaddress

#host to listen
HOST = '192.168.1.106'

#1 maps the first 20bytes into a readable buffer
class IP:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        #assign to ver only the high order nybble(right shift by 4 places)
        self.ver = header[0] >> 4
        #second nibble doing AND (0xF = 00001111)
        self.ihl = header[0] & 0xF
        
        #Now that is decoded we can get the info from the packet
        self.ts = header[1]
        self.len = header[2]
        self.id = header[3]
        self.off = header[4]
        self.ttl = header[5]
        self.proto_num = header[6]
        self.sum = header[7]
        self.who = header[8]
        self.to = header[9]
        
        #readable ips
        self.who_address = ipaddress.ip_address(self.who)
        self.to_address = ipaddress.ip_address(self.to)
        
        #protocol constants -> 1: ICMP, 6:TCP, 17:UDP
        self.proto_map = {1: 'ICMP', 6:'TCP', 17:'UDP'}
        try:
            self.proto = self.proto_map[self.proto_num]
        
        except Exception as e:
            print('%s No protocol for %s' % (e, self.proto_num))
            self.protocol = str(self.proto_num) 
               
def snifit():
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
    
    #read a packet till user stops
    try:
        while True:
            buffer_og = snifit.recvfrom(65565)[0]
            #IP header (20bytes)
            ip_head = IP(buffer_og[0:20])
            #print a readable mess
            print('Protocol: %s %s -> %s' % (ip_head.proto,ip_head.who_address,ip_head.to_address))
            
    except KeyboardInterrupt:
        #WIndows? turn off prom mode
        if os.name == 'nt':
            snifit.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            sys.exit()
        
    
    

if __name__ == '__main__':
    snifit()  
            
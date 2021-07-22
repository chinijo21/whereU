#gets the location of the machine using geolite2 and requests
import requests
from geolite2 import geolite2

def ip_pos(actual_ip):
    print(actual_ip)
    
#ipify API   
actual_ip = requests.get('https://api.ipify.org').text

ip_pos(actual_ip)
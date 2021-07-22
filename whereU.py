#gets the location of the machine using geolite2 and requests
import requests
from geolite2 import geolite2

def ip_pos(actual_ip):
    pos_byIp = geolite2.reader()
    location = pos_byIp.get(actual_ip)
    
    #geolite database dict values and fine tunning
    a=(location['city']['names']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])

    print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s\n'''
     % (a,b,c,d,e,f,g))
    
    
#ipify API   
actual_ip = requests.get('https://api.ipify.org').text
ip_pos(actual_ip)
from requests import get
import json

def get_location():
    ip_info=json.loads(get('https://ipinfo.io/json').text)
    return(ip_info["loc"])
    #return(ip_info["city"])

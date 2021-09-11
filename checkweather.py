import checkip
import requests
from bs4 import BeautifulSoup

def get_weather():
    location=checkip.get_location()
    #headers = {
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',"accept-language":"en-US"}
    res=requests.get("https://weather.com/weather/today/l/"+location)
    #soup = BeautifulSoup(res.text, 'html.parser')
    """
    f=open("res.txt","w+")
    f.write(res.text)
    f.close()
    """
    #print(res.text)
    #if 'CurrentConditions--dataWrapperInner--200v2' in res.text:
    #    print("yes")
    #info = soup.select('CurrentConditions--dataWrapperInner--200v2')[0].get_text()
    text=""
    for i in res.text.splitlines():
        if 'CurrentConditions--dataWrapperInner--200v2' in i:
            soup = BeautifulSoup(i, 'html.parser')
            text=text+soup.get_text()
    finaltext=text.split("ForecastAdvertisement")[-1]
    data_clear=["clear","sunny"]
    data_fog=["haze,fog"]
    data_rain=["shower","rain"]
    data_thunder=["thunder"]
    for i in data_clear:
        if i in finaltext:
            return("clear")
    for i in data_fog:
        if i in finaltext:
            return("fog")
    for i in data_rain:
        if i in finaltext:
            return("rain")
    for i in data_thunder:
        if i in finaltext:
            return("thunder")


    #print(info)

get_weather()

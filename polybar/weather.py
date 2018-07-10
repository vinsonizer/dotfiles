#!/bin/python

import urllib.request, json, os, sys, datetime

ow_api_key = os.environ['OW_API']
ip_api_key = os.environ['IP_API']
city = "Tega%20Cay"
units = "Imperial"
unit_key = "F"

ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

location = eval(urllib.request.urlopen("http://api.ipstack.com/{}?access_key={}&fields=latitude,longitude,city".format(ip, ip_api_key)).read().decode("utf8"))

lat = location["latitude"]
long = location["longitude"]
city = location["city"]

if city and len(city) > 0:
    city = city + ": "

if(len(sys.argv) == 1):
    weather = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}&units={}".format(lat, long, ow_api_key, units)).read())[2:-1])
    info = weather["weather"][0]["description"].title()
    temp = int(float(weather["main"]["temp"]))

    print("%s%s, %i °%s" % (city, info, temp, unit_key))
else:
    forecast = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&APPID={}&units={}".format(lat, long, ow_api_key, units)).read())[2:-1])
    print(forecast)
    #datetime.date.fromtimestamp(1485799200).weekday()

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
    forecast = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast/daily?cnt=5&lat={}&lon={}&APPID={}&units={}".format(lat, long, ow_api_key, units)).read())[2:-1])
    #print("http://api.openweathermap.org/data/2.5/forecast/daily?cnt=5&lat={}&lon={}&APPID={}&units={}".format(lat, long, ow_api_key, units))
    dayMap = {
        0 : "Monday   ",
        1 : "Tuesday  ",
        2 : "Wednesday",
        3 : "Thursday ",
        4 : "Friday   ",
        5 : "Saturday ",
        6 : "Sunday   "}

    def extractDay(dt):
        return dayMap[datetime.date.fromtimestamp(dt).weekday()]

    def extractWeather(x):
        return x["weather"][0]["main"] + " - "

    def extractTemp(x):
        return str(int(x["temp"]["min"])) + "/" + str(int(x["temp"]["max"]))

    def getForecast(x):
        return extractDay(x["dt"]) + " " + extractWeather(x) + " " + extractTemp(x)

    flist = list(map((lambda x: getForecast(x)), forecast["list"]))
    print('%s<br/>%s' % (forecast["city"]["name"], '\n'.join(map(str, flist))))

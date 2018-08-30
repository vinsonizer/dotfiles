#!/bin/python

import urllib.request, json, os, sys, datetime
from weather import Weather, Unit

ow_api_key = os.environ['OW_API']
ip_api_key = os.environ['IP_API']

# Where are we?
ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')

location = eval(urllib.request.urlopen("http://api.ipstack.com/{}?access_key={}&fields=latitude,longitude,city".format(ip, ip_api_key)).read().decode("utf8"))

lat = location["latitude"]
long = location["longitude"]

weather = Weather(unit=Unit.FAHRENHEIT)
lookup = weather.lookup_by_latlng(lat, long)

# Get Current Weather
if(len(sys.argv) == 1):
    condition = lookup.condition
    print("%s, %s °F" % (condition.text, condition.temp))
    print(lookup.__dict__)

# Get Forecast
else:
    forecast = lookup.forecast

    def getForecast(x):
      return x.day + ": " + x.high + "/" + x.low + " - " + x.text

    flist = list(map((lambda x: getForecast(x)), lookup.forecast))

    print('%s' % ('\n'.join(map(str, flist))))

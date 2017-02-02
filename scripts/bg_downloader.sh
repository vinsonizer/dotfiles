#!/bin/bash

i3proc=$(ps -u jason | grep i3 | awk {'print $1'})
d=$(cat /proc/$i3proc/environ | tr '\0' '\n' | grep '^DISPLAY=' | awk -F = {'print $2'})

curl -sS 'https://unsplash.it/1920/1080/?random' | DISPLAY=$d feh --bg-fill -

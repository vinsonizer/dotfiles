#!/bin/bash

scrot /tmp/bg.png && mogrify -blur 2x8 /tmp/bg.png
/usr/bin/i3lock -i /tmp/bg.png

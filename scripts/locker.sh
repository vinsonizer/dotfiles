#!/bin/bash

scrot /tmp/bg.png && mogrify -blur 4x8 /tmp/bg.png
/usr/bin/i3lock -i /tmp/bg.png
/usr/bin/dm-tool switch-to-greeter

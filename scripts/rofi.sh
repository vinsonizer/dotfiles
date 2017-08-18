#!/bin/bash

width=50
lines=10
columns=2

bgimage=$( cat ${HOME}/.fehbg | awk {'print $3'} | tr \' ' ')

## Pull 4 main colors from background file
#colors=$(convert /tmp/bg.jpg -scale 1x3\! txt:- | awk {' print $3 '} | tail -3 | sort -r | paste -s -d ,)

#rofi -modi "drun,window" -show drun -sidebar-mode -width $width -lines $lines -columns $columns #-color-window "$colors"

rofi -show drun -sidebar-mode -width $width -lines $lines -columns $columns -fake-transparency

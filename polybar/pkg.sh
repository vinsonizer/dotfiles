#!/bin/bash
pac=$(checkupdates | wc -l)
aur=$(cower -u | wc -l)

check=$((pac + aur))
if [[ "$check" != "0" ]]
then
    echo "$check updates"
    #echo "$pac %{F#5b5b5b}%{F-} $aur"
    #/usr/bin/notify-send "Package Updates" "Found $pac Core and $aur AUR Updates"
else
    echo ""
fi

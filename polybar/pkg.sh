#!/bin/bash


sudo /usr/bin/yay -Sy > /dev/null 2>&1

check=$(yay -Pn)
if [[ "$check" != "0" ]]
then
    echo "$check updates"
else
    echo ""
fi

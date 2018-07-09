#!/bin/bash


/usr/bin/yay -Sy

check=$(yay -Pn)
if [[ "$check" != "0" ]]
then
    echo "$check updates"
else
    echo ""
fi

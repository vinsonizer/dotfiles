#!/bin/bash

cd ${HOME}/.dotfiles
export x=$(git fetch origin && git diff origin | grep "@@")

if [[ "$x1" -ne "1" ]]; then
	echo ""
fi

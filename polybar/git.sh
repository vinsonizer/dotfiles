#!/bin/bash

cd ${HOME}/.dotfiles
export x=$(git fetch origin && git diff origin | grep "@@" | head -1 | wc -l)
echo $x

if [[ "$x" -eq "1" ]]; then
	echo ""
fi

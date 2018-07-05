#!/bin/bash

cd ${HOME}/.dotfiles
export x="x$(git fetch origin && git diff origin | grep "@@" | head -1)"

if [[ "$x" != "x" ]]; then
	echo ""
else
	echo ""
fi

#!/bin/python

import json, os

home = os.environ['HOME']

with open(home + "/.config/Google Play Music Desktop Player/json_store/playback.json") as f:
    data = json.load(f)

artist= data["song"]["artist"]
title = data["song"]["title"]

print("%s: %s" % (artist, title))

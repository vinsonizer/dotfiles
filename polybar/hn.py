#!/usr/bin/python

import feedparser
import time


while True:
    feed = feedparser.parse("https://hnrss.org/frontpage")

    for entry in feed.entries:
        fh = open('/tmp/hn.url', 'w')
        fh.write(entry.link)
        fh.close()
        print(entry.title)
        time.sleep(30)

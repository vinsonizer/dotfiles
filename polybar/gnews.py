#!/usr/bin/python

import feedparser
import time


while True:
    feed = feedparser.parse("https://news.google.com/news/rss/?ned=us&gl=US&hl=en")

    for entry in feed.entries:
        fh = open('/tmp/gnews.url', 'w')
        fh.write(entry.link)
        fh.close()
        print(entry.title)
        time.sleep(30)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

emojis = {}
for tweet in tweets:
    for char in list(tweet): # XXX really silly way!
        if len(str.encode(char)) >= 4: # check utf8mb4 or not
            emojis[char] = True

for emoji in emojis.keys():
    print(emoji)

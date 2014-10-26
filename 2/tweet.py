#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def load_tweets():
    fh = open('./resource/tweet.txt', encoding="utf-8")
    rows = [row.rstrip('\r\n') for row in fh.readlines()];

    tweet = ''
    tweets = []
    is_before_blank = False;
    re4username = re.compile('[0-9a-zA-Z_]+ : ')

    for row in rows:
        if row == '':
            is_before_blank = True;
        else:
            if is_before_blank == True and re4username.match(row):
                tweets.append(tweet)
                tweet = ''

            tweet += row + '\n'
            is_before_blank = False

    return tweets


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_now = re.compile('なう\Z')
for tweet in tweets:
    tweet = tweet.rstrip('\r\n')
    if re_now.search(tweet):
        print(tweet);


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_rt_comment = re.compile('[0-9a-zA-Z_]+ : (.+?)RT @')
for tweet in tweets:
    matched = re_rt_comment.match(tweet)
    if matched:
        print(matched.group(1));

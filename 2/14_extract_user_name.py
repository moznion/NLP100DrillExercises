#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_user_name = re.compile('@[0-9a-zA-Z_]+')
for tweet in tweets:
    matched = re_user_name.search(tweet)
    if matched:
        print(matched.group(0));

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_paren = re.compile('([\u4e00-\u9fa5]+?)([(（][A-Z]+?[）)])')
for tweet in tweets:
    matched = re_paren.search(tweet)
    if matched:
        print(matched.group(1) + "\t" + matched.group(2));


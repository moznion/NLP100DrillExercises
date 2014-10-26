#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_kakusan = re.compile('拡散希望')
for tweet in tweets:
    if re_kakusan.search(tweet):
        print(tweet);

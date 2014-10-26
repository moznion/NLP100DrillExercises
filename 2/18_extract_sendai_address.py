#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_sendai = re.compile('(?:青葉|宮城野|若林|太白|泉)区[\u4e00-\u9fa5あ-ん0-9０-９]+')
for tweet in tweets:
    matched = re_sendai.search(tweet)
    if matched:
        print(matched.group(0));


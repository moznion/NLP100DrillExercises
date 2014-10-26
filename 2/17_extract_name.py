#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_name = re.compile('([\u4e00-\u9fa5]+?|[あ-ん]+?|[ア-ン]+?)(?:さん|君|くん|氏|ちゃん)')
for tweet in tweets:
    matched = re_name.search(tweet)
    if matched:
        print(matched.group(1));


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_user_name = re.compile('@([0-9a-zA-Z_]+)')
for tweet in tweets:
    tweet = re_user_name.sub('<a href="https://twitter.com/#!/\g<1>">@\g<1></a>', tweet)
    print(tweet)


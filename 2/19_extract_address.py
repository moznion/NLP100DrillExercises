#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tweet

tweets = tweet.load_tweets()

re_postal_code = re.compile('[0-9０-９]{3}-[0-9０-９]{4}')
re_prefecture = re.compile('(?:北海道|東京都|(?:大阪|京都)府|(?:青森|岩手|宮城|秋田|山形|福島|茨城|栃木|群馬|埼玉|千葉|神奈川|新潟|富山|石川|福井|山梨|長野|岐阜|静岡|愛知|三重|滋賀|兵庫|奈良|和歌山|鳥取|島根|岡山|広島|山口|徳島|香川|愛媛|高知|福岡|佐賀|長崎|熊本|大分|宮崎|鹿児島|沖縄)県)')
re_address = re.compile('([\u4e00-\u9fa5あ-んア-ン]+?[市区郡町村字])')

address_dict = {
    'postal_code': {},
    'prefecture': {},
    'address': {},
}

for tweet in tweets:
    postal_code_matched = re_postal_code.search(tweet)
    if postal_code_matched:
        postal_code = postal_code_matched.group(0)
        if postal_code:
            address_dict['postal_code'][postal_code] = True

    prefecture_matched = re_prefecture.search(tweet)
    if prefecture_matched:
        prefecture = prefecture_matched.group(0)
        if prefecture:
            address_dict['prefecture'][prefecture] = True

    address_matched = re_address.search(tweet)
    if address_matched:
        address = address_matched.group(0)
        if address:
            address_dict['address'][address] = True

for group, dic in address_dict.items():
    print(group)
    for key in dic.keys():
        print(key)
    print()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

fh = open('./col1.txt', encoding='utf-8')

rows = list(map(lambda row: row.rstrip('\r\n'), fh.readlines()))
print(len(list(set(rows))))

# check cmd
# $ cut -f 1 ./resource/address.txt | sort | uniq | wc

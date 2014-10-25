#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

fh = open('./col2.txt', encoding='utf-8')

group_by_count = {}
for row in fh.readlines():
    key = row.rstrip('\r\n')
    if not key in group_by_count:
        group_by_count[key] = 0
    group_by_count[key] += 1

for group, count in sorted(group_by_count.items(), key=lambda item: item[1], reverse=True):
    print(group)


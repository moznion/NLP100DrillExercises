#!/usr/bin/env python
# -*- coding: utf-8 -*-

fh = open('./resource/address.txt', encoding='utf-8')
rows = [row.rstrip('\r\n') for row in fh.readlines()]
rows_tuple = [tuple(row.split('\t')) for row in rows]

sorted_rows = sorted(rows_tuple, key=lambda row: row[1], reverse=True)
for row in sorted_rows:
    print(row[0] + '\t' + row[1])

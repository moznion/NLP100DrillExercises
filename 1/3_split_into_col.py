#!/usr/bin/env python
# -*- coding: utf-8 -*-

fh = open('resource/address.txt', encoding='utf-8')
rows = fh.readlines()

fh_to_write_col1 = open('col1.txt', 'w')
fh_to_write_col2 = open('col2.txt', 'w')
for row in rows:
    row  = row.rstrip('\r\n')
    cols = row.split('\t')
    fh_to_write_col1.write(cols[0] + '\n')
    fh_to_write_col2.write(cols[1] + '\n')


#!/usr/bin/env python
# -*- coding: utf-8 -*-

fh_col1 = open('col1.txt', encoding='utf-8')
fh_col2 = open('col2.txt', encoding='utf-8')

col1_rows = fh_col1.readlines()
col2_rows = fh_col2.readlines()

for row_tuple in zip(col1_rows, col2_rows):
    col1 = row_tuple[0].rstrip('\r\n')
    col2 = row_tuple[1].rstrip('\r\n')
    print(col1 + '\t' + col2)


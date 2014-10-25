#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

fh = open('./resource/address.txt', encoding='utf-8')
rows = fh.readlines()

line_num = int(sys.argv[1])

for row in rows[-line_num:]:
    print(row.rstrip('\r\n'))

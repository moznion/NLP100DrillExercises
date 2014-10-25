#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

fh = open('resource/address.txt', encoding='utf-8')
address_text  = fh.read();
replaced_text = address_text.replace('\t', ' ')

print(replaced_text)


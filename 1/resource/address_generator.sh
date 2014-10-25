#!/bin/sh

set -e
set -x

wget --quiet http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip --output-document=/tmp/ken_all.zip
unzip -o /tmp/ken_all.zip -d /tmp
nkf -w --overwrite /tmp/KEN_ALL.CSV

cat /tmp/KEN_ALL.CSV | ./address.py > address.txt


#!/bin/sh

set -x

./11_extract_kakusan.py
./12_extract_now.py
./13_extract_unofficial_rt_comment.py
./14_extract_user_name.py
./15_substitute_twitter_id_to_link.py
./16_extract_paren_contents.py
./17_extract_name.py
./18_extract_sendai_address.py
./19_extract_address.py
./20_extract_emoji.py


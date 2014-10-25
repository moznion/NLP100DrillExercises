#!/bin/sh

set -x

./01_count_rows.py
./02_replace_tab_to_space.py
./03_split_into_col.py
./04_concat.py
./05_head.py 10
./06_tail.py 10
./07_uniq_group_num.py
./08_sort_by_asc.py
./09_sort_by_desc.py
./10_freq.py


#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("./data/hightemp.txt") as f:
    pre_set = set()
    for line in f:
        pre_set.add(line.split()[0].decode('utf-8'))
for w in pre_set:
    print(w)        #ASCII文字列でないので print(pre_set)としてもうまく出力できない

# Unix command
# cut -f 1 ./data/hightemp.txt | sort | uniq

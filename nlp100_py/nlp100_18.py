#!/usr/bin/env python
# -*- coding: utf-8 -*-

# with open("./data/hightemp.txt") as f:
#     lines = [l.split() for l in f]
# lines.sort(key = lambda l: l[2], reverse = True)
# for l in lines:
#     print('\t'.join(l))

with open("./data/hightemp.txt") as f:
    lines = f.readlines()
lines.sort(key=lambda l: float(l.split()[2]), reverse=True)
for l in lines:
    print(l.rstrip('\n'))

# Unix command
# sort -r -k 3 ./data/hightemp.txt

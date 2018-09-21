#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def head(path, num):
    with open(path) as f:
        for i in range(num):
            sys.stdout.write(f.readline())
            #print(f.readline().rstrip("\n"))

# def head(path, num):
#     with open(path) as f:
#     for i, line in enumerate(f):
#         if i >= n:
#             break
#         print(line.rstrip())

print("how manu lines do you want?")
num = int(raw_input())
path = "./nlp100/hightemp.txt"
head(path, num)

# Unix command
# read N
# head -n $N ./nlp100/hightemp.txt

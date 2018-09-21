#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tail(path, num):
    with open(path) as f:
        lines = f.readlines()
        for line in lines[-num:]:
            print(line.rstrip())

print("how manu lines do you want?")
num = int(raw_input())
path = "./nlp100/hightemp.txt"
tail(path, num)

# Unix command
# read N
# tail -n $N ./nlp100/hightemp.txt

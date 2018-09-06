#!/usr/bin/env python
# -*- coding: utf-8 -*-

def split(path, num):
    with open(path) as source_file:
        lines = source_file.readlines()
    file_size = -(-len(lines) // num)   #切り上げの計算
    print(file_size)
    # for n in range(1, num+1):
    #     with open(path.rstrip(".txt") + "_split%d.txt" % n, 'w') as f:
    #         for line in lines[file_size*(n-1):file_size*n]:
    #             f.write(line)  #printは自動で改行が挿入されるがwriteは挿入されない
    for n, offset in enumerate(range(0, len(lines), file_size), 1):
        with open(path.rstrip(".txt") + "_split%d.txt" % n, 'w') as f:
            for line in lines[offset : offset + file_size]:
                f.write(line)  #printは自動で改行が挿入されるがwriteは挿入されない

print("how manu lines do you want?")
num = int(raw_input())
path = "./nlp100/hightemp.txt"
split(path, num)

# Unix command

# read N
# len=$(cat ./data/hightemp.txt | wc -l)
# len=$(wc -l ./data/hightemp.txt | awk '{print $1}')
# file_size=$((-(-$len/$N)))
# split -l $file_size ./data/hightemp.txt ./data/hightemp_split_u  #BSD
# split -l $file_size -d --additional-suffix=.txt ./data/hightemp.txt ./data/hightemp_split_u  #Linux

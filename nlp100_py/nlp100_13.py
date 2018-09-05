#!/usr/bin/env python
# -*- coding: utf-8 -*-

def file_merge(path1, path2, merge_path):
    with open(path1, 'r') as f1, \
          open(path2, 'r') as f2,\
          open(merge_path, 'w') as mf:
        for l1, l2 in zip(f1, f2):
            mf.write(l1.rstrip("\n") + "\t" + l2)

path1 = "./nlp100/col1.txt"
path2 = "./nlp100/col2.txt"
merge_path = "./nlp100/col_merge.txt"
file_merge(path1, path2, merge_path)

# unix command
# paste ./nlp100/col1.txt ./nlp100/col2.txt > ./nlp100/col_merge_u.txt
# diff --report-identical-files ./nlp100/col_merge.txt ./nlp100/col_merge_u.txt

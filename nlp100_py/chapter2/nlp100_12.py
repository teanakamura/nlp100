#!/usr/bin/env python
# -*- coding: utf-8 -*-

# col_n = 2
# f = [''] * col_n
# with open("./nlp100/hightemp.txt") as source_file:
#         for i, j in enumerate(range(col_n), 1):
#              f[j] = open("./nlp100/col%d.txt" % i, 'w')
#         for line in source_file:
#             for j in range(col_n):
#                 f[j].write(line.split()[j] + "\n")
#         # line = source_file.readline()
#         # while line:
#         #     for j in range(col_n):
#         #         f[j].write(line.split()[j] + "\n")
#         #     line = source_file.readline()
#         for j in range(col_n):
#             f[j].close

def col_file(num):
    with open("./nlp100/hightemp.txt") as source_file:
        with open("./nlp100/col%d.txt" % num , 'w') as f:
            for line in source_file:
                f.write(line.split()[num-1] + "\n")

col_file(1)
col_file(2)


# Unix command
# cut -f 1 ./nlp100/hightemp.txt > ./nlp100/col1.txt
# cut -f 2 ./nlp100/hightemp.txt > ./nlp100/col2.txt

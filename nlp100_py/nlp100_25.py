#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json
import re

def extract_UK():
    with gzip.open("data/jawiki-country.json.gz") as f:
        for line in f:
            doc = json.loads(line)
            if doc['title'] == u'イギリス':
                return doc['text']

# pattern1 = re.compile(u'{{基礎情報.+?}}\n', re.DOTALL)
    # re.DOTALL で"."が改行文字にもマッチするようになる
    # "\n"の代わりにre.M で"$"を使用しても良い。
    # 本来は{{}}の数を数えるべきだが難しいので簡易的に改行前の}}のマッチで判断するようにした。
pattern1 = r'{{基礎情報(?:(?:[^{}]*{{[^{]+}})*[^{]*)}}'.decode('utf-8')
    # こっちの方がいいかも。ただ多重の{{}}には対応できない。
pattern2 = re.compile(r'\|(.+?)\s*=[\t\r\f\v]*(.*?)(?=\n\||\n\}\})', re.DOTALL)

all_base_info = re.findall(pattern1, extract_UK())
base_infoes = re.findall(pattern2, all_base_info[0])
result = {info[0]:re.sub(r'<.+>', '', info[1]) for info in base_infoes}  # dictの内包表記

# for key, value in result.items():
#     print(key + ":" + value)

# dict型は順番が追加順でないので出力順を調整して確認しやすくするには以下
order = [info[0] for info in base_infoes]  # keyの順番を保存するための変数を用意する。listの内包表記
for key in order:
    print(key + ":" + result[key])

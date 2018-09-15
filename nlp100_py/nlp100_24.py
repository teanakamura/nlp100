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

# セクションはマークアップ記法の見出しの階層のこと。多分
pattern = re.compile(r'^.*(ファイル|File):(.+?)(?:\|.+)?$'.decode('utf-8'), re.M)
    # python2ではユニコード文字列を指定しないと”ファイル”にマッチしない。
    # uフラグで記述するか r'regex'.decode(utf-8) とする。uフラグで記述する際はエスケープ処理に注意。
    # python3ではデフォルトでユニコード文字列なので気にせず全てrフラグで記述すれば良い。
files = re.findall(pattern, extract_UK())
for afile in files:
    print(afile[1])

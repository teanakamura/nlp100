#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import json

with gzip.open("data/jawiki-country.json.gz") as f:
    for line in f:
        doc = json.loads(line)
        if doc['title'] == u'イギリス':
            print(doc['text'])
            break

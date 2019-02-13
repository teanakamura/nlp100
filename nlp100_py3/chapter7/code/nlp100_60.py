"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

from IPython import embed
from mymodule.path_helpers import get_rel_path_from_working_directory
import json
import redis
import sys

def create_name_area_kvs(json_file_path):
    with open(json_file_path) as f:
        dic = {}
        mapping_num = 0
        mapping_size = 1024 ** 2 / 2 - 1 # redis commandに渡せる引数の最大数
        for i, line in enumerate(f, 1):
            data = json.loads(line)
            name = data.pop('name')
            area = data.pop('area', 'None')
            dic[name] = area
            if i == mapping_num * mapping_size + 1:
                if i != 1:
                    print ('')
                    r.mset(dic)
                dic = {}
                print('%d - %dth line' % (mapping_num * mapping_size + 1, (mapping_num + 1) * mapping_size))
                mapping_num += 1
            sys.stdout.write('\r%d' % i)  # consoleに上書き出力
        print('')

if __name__ == '__main__':
    # r = redis.Redis(host='localhost', port=6379, db=0)
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool)
    json_file = get_rel_path_from_working_directory(__file__, '../data/artist.json')
    create_name_area_kvs(json_file)

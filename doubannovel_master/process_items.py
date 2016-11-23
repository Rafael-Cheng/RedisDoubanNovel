#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import redis
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    r = redis.StrictRedis(host='127.0.0.1', port=6379)
    f = open('items.json', 'a+')
    while True:
        print "in loop"
        try:
            data = r.lpop("douban:items")
            item = json.loads(data)
            f.write(json.dumps(item['name'], ensure_ascii=False) + '\n')
        #need more exception handeling methodg
        except Exception:
            break
    f.close() 
    print "done"
 
if __name__ == '__main__':
    main()

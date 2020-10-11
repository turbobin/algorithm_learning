#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/4/11'

class LRUcache:
    """python dict 不跟踪插入顺序，所以要维护一个dict记录顺序"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def set(self, key, value):
        if len(self.cache) > self.capacity:
            old_key = min(self.cache.keys, key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)

        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cachep[key]

        return -1



# 使用有序字典(推荐)
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def set(self, key, value):

        if key in self.cache:
            self.cache.pop(key)

        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  
            # 只有OrderedDict才有popitem(last=Flase)这个参数，
            # dict的popitem()里不能加参数
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = value
            return value

        return None

if __name__ == '__main__':
    lrucache = LRUCache(5)
    lrucache.set(1, "a")
    lrucache.set(3, "b")
    lrucache.set(2, "c")
    lrucache.set(3, "d")
    lrucache.set(4, "e")
    lrucache.set(6, "f")

    print(lrucache.cache)
    print(lrucache.get(2))
    print(lrucache.cache)

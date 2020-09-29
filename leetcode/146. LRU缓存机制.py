#coding:utf-8

'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

'''
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        v = self.dic.get(key, -1)
        if key in self.dic:
            self.dic.move_to_end(key, last=True)
        return v

    def put(self, key, value):
        self.dic[key] = value
        self.dic.move_to_end(key, last=True)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False) # FIFO

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
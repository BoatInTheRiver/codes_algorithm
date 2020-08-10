#coding:utf-8
'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

'''

class MaxQueue:
    def __init__(self):
        self.queue = []

    def max_value(self):
        if not self.queue:
            return -1
        return max(self.queue)

    def push_back(self, value):
        self.queue.append(value)

    def pop_front(self):
        if not self.queue:
            return -1
        return self.queue.pop(0)
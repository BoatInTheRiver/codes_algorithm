#coding:utf-8
'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

'''

class MaxQueue:
    def __init__(self):
        self.queue = []
        self.stack = []

    def max_value(self):
        if not self.stack:
            return -1
        return self.stack[0]

    def push_back(self, value):
        self.queue.append(value)
        while self.stack and self.stack[-1] < value:
            self.stack.pop()
        self.stack.append(value)

    def pop_front(self):
        if not self.queue:
            return -1
        res = self.queue.pop(0)
        if res == self.stack[0]:
            self.stack.pop(0)
        return res
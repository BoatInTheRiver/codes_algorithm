#coding:utf-8
'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )

示例：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
'''

class CQueue:
    def __init__(self):
        self.a = []
        self.b = []

    def appendTail(self, value):
        self.a.append(value)

    def deleteHead(self):
        if self.b:
            return self.b.pop()
        if not self.a and not self.b:
            return -1
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
#coding:utf-8
'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

'''

class MedianFinder:
    def __init__(self):
        self.res = []

    def addNum(self, num):
        self.res.append(num)

    def findMedian(self):
        self.res.sort()
        n = len(self.res)
        if n % 2 == 1:
            return self.res[n // 2]
        else:
            return (self.res[n // 2 - 1] + self.res[n // 2]) / 2
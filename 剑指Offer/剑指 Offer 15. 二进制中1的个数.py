#coding:utf-8
'''
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

'''

class Solution:
    def hammingWeight(self, n):
        s = str(n)
        count = 0
        for c in s:
            if c == '1':
                count += 1
        return count

    def hammingWeight1(self, n):
        '''逐个判断，使用与运算'''
        res = 0
        while n:
            res += n & 1
            n >>= 1 # 无符号右移一位
        return res
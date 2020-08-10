#coding:utf-8
'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

class Solution:
    def sumNums(self, n):
        return n != 0 and n + self.sumNums(n - 1)
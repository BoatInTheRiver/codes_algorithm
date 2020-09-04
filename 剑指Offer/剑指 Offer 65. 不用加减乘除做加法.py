#coding:utf-8
'''
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
'''

class Solution:
    def add(self, a, b):
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = a ^ b, (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

# print(hex(1 & 0xffffffff))
# print(hex(-1 & 0xffffffff))
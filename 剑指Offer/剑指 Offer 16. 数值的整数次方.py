#coding:utf-8
'''
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。

'''

class Solution:
    def pow(self, x, n):
        if x == 0:
            return 0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res
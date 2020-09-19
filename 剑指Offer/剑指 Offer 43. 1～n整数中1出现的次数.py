#coding:utf-8

'''
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例：
输入：n = 12
输出：5
'''

class Solution:
    def countDigitOne(self, n):
        if n == 0:
            return 0
        s = str(n)
        high = int(s[0])
        power = 10**(len(s) - 1)
        remain = n - high * power
        if high == 1:
            return self.countDigitOne(power - 1) + remain + 1 + self.countDigitOne(remain)
        else:
            return self.countDigitOne(power - 1) * high + power + self.countDigitOne(remain)
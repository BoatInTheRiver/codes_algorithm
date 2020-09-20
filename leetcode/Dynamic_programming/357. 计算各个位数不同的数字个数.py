#coding:utf-8

'''
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:
输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

'''

'''
当n = 0,个数为1
当n = 1,个数为10
当n = 2,个数为 10 + 9 * 9
当n = 3,个数为 10 + (10 + 9 * 9) + (10 + 9 * 9 + 9 * 9 * 8)
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        a, b = 10, 9 * 9
        for i in range(2, min(n, 10) + 1):
            a += b
            b *= (10 - i)
        return a 
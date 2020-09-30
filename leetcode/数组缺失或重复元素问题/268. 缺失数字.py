#coding:utf-8

'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
'''

'''
数学方法: 0-n的连续数字的和为n*(n+1)/2

'''

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
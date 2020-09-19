#coding:utf-8

'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
'''

class Solution:
    def maxProduct(self, nums):
        res, imax, imin = float('-inf'), 1, 1
        for num in nums:
            if num > 0:
                imax = max(imax * num, num)
                imin = min(imin * num, num)
            else:
                tmp = imax
                imax = max(imin * num, num)
                imin = min(tmp * num, num)
            res = max(res, imax)
        return res
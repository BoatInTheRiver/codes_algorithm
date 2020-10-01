#coding:utf-8

'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例:
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
'''

class Solution:
    def subarraySum(self, nums, k):
        dic = {0:1}
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in dic:
                res += dic[cur_sum - k]
            dic[cur_sum] = dic.get(cur_sum, 0) + 1
        return res
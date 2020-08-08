#coding:utf-8
'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res
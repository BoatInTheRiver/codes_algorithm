#coding:utf-8

'''
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
'''

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] 赋值有先后，这种是错的
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
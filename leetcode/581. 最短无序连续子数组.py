#coding:utf-8

'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
你找到的子数组应是最短的，请输出它的长度。

示例:
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

'''

class Solution:
    '''排序'''
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        left, right = len(nums) - 1, 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left = min(left, i)
                right = max(right, i)
        return right - left + 1 if right > left else 0

    '''双指针'''
    def findUnsortedSubarray1(self, nums):
        ma, mi = nums[0], nums[-1]
        left, right = 0, -1
        n = len(nums)
        for i in range(n):
            if nums[i] < ma:
                right = i
            else:
                ma = nums[i]
            if nums[n - i - 1] > mi:
                left = n - i - 1
            else:
                mi = nums[n - i - 1]
        return right - left + 1
#coding:utf-8
'''
统计一个数字在排序数组中出现的次数。
'''

class Solution:
    def search(self, nums, target):
        def helper(tar):
            i, j = 0, len(nums) - 1
            mid = (i + j) // 2
            while i <= j:
                if nums[i] <= tar:
                    i = mid + 1
                else:
                    j = mid - 1
            return i
        return helper(target) - helper(target - 1)
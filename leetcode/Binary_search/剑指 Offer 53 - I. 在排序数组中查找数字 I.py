#coding:utf-8

'''
统计一个数字在排序数组中出现的次数。

示例:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
'''

'''
通过搜索n和n-1 的右边界来得到n的个数
'''
class Solution:
    def search(self, nums, target):
        def helper(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        return helper(target) - helper(target - 1)
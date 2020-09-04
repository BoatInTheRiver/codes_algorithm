#coding:utf-8

'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
'''

class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        i, j = 0, len(nums) - 1
        res =[]
        # 找左边界
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                j = mid - 1
        if i >= len(nums) or nums[i] != target:
            return [-1, -1]
        res.append(i)
        i, j = 0, len(nums) - 1
        # 找右边界
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        if j < 0 or nums[j] != target:
            return [-1, -1]
        res.append(j)
        return res

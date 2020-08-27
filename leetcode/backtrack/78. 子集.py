#coding:utf-8

'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
'''

class Solution:
    def subsets(self, nums):
        res = []
        self.backtrack(nums, 0, [], res)
        return res

    def backtrack(self, nums, index, path, res):
        res.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path, res)
            path.pop()
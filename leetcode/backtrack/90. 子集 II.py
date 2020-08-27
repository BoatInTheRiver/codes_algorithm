#coding:utf-8

'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集
'''

class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        if n == 0:
            return []
        res = []
        nums.sort()
        used = [False] * n
        self.backtrack(nums, 0, [], used, res)
        return res

    def backtrack(self, nums, index, path, used, res):
        res.append(path[:])
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, i+1, path, used, res)
            used[i] = False
            path.pop()
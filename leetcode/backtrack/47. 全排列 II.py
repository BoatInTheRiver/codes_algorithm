#coding:utf-8

'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。
'''

class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        if n == 0:
            return []
        res = []
        nums.sort()
        used = [False] * n
        self.backtrack(nums, [], used, res)
        return res

    def backtrack(self, nums, path, used, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                self.backtrack(nums, path, used, res)
                used[i] = False
                path.pop()
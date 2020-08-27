#coding:utf-8

'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
'''

import itertools

class Solution:
    '''利用库函数'''
    # def permute1(self, nums):
    #     return list(itertools.permutations(nums))
    def permute(self, nums):
        '''回溯'''
        res = []
        n = len(nums)
        used = [False] * n
        self.backtrack(nums, 0, n, [], used, res)
        return res

    def backtrack(self, nums, depth, n, path, used, res):
        if len(path) == n:
            res.append(path[:])
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.backtrack(nums, depth + 1, n, path, used, res)
                used[i] = False
                path.pop()
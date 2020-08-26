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
        def backtrack(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                backtrack(nums, tmp)
                tmp.pop()
        backtrack(nums, [])
        return res

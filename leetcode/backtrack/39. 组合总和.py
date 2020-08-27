#coding:utf-8

'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

'''

class Solution:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        if n == 0:
            return []
        res = []
        candidates.sort()
        self.backtrack(candidates, 0, n, target, [], res)
        return res


    def backtrack(self, candinates, begin, n, target, path, res):
        if target == 0:
            res.append(path[:])
            return
        for i in range(begin, n):
            if target - candinates[i] < 0:
                break
            path.append(candinates[i])
            self.backtrack(candinates, i, n, target-candinates[i], path, res)
            path.pop()
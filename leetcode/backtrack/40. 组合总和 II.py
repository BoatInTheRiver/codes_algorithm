#coding:utf-8

'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

'''

class Solution:
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        if n == 0:
            return []
        res = []
        candidates.sort()
        self.backtrack(candidates, 0, n, target, [], res)
        return res

    def backtrack(self, candidates, begin, n, target, path, res):
        if target == 0:
            res.append(path[:])
            return
        for i in range(begin, n):
            # 大剪枝，因为此时的candidates是有序数组
            if target - candidates[i] < 0:
                break
            if i > begin and candidates[i - 1] == candidates[i]:
                continue
            path.append(candidates[i])
            # 元素不可重复使用，所以递归传递下去的是i + 1而不是i
            # 如果第一个数和第二个数相等，第一个数考虑的数组范围更大，而第二个数得到的结果肯定是重复的，得减掉
            self.backtrack(candidates, i+1, n, target-candidates[i], path, res)
            path.pop()
#coding:utf-8

'''
给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。
每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

本题与leetcode第877题 石子游戏解法完全相同
'''

class Solution:
    '''递归'''
    def predictTheWinner1(self, nums):
        def helper(start, end):
            if start == end:
                return nums[start]
            pickstart = nums[start] - helper(start + 1, end)
            pickend = nums[end] - helper(start, end - 1)
            res = max(pickstart, pickend)
            return res
        return helper(0, len(nums) - 1) >= 0

    '''备忘录'''
    def predictTheWinner2(self, nums):
        memo = {}
        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start == end:
                memo[(start, end)] = nums[start]
                return nums[start]
            pickstart = nums[start] - helper(start + 1, end)
            pickend = nums[end] - helper(start, end - 1)
            memo[(start, end)] = max(pickstart, pickend)
            return memo[(start, end)]
        return helper(0, len(nums) - 1) >= 0

    '''动态规划'''
    '''
    甲乙比赛，甲先手面对区间[i,...,j]时，dp[i][j]表示甲对乙的净胜分,返回结果dp[0][n-1]是否大于等于0
    
    '''
    def predictTheWinner3(self, nums):
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n-1] >= 0

    '''动态规划空间优化版本'''

    def predictTheWinner4(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = nums[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[n - 1] >= 0
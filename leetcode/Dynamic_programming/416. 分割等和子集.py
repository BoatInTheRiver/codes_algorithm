#coding:utf-8

'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
'''

'''
思路：
将问题转化为背包问题，给一个可装载重量为(sum // 2)的背包和n个物品，每个物品的重量为nums[i],是否存在一种方法，把背包装满。
'''
class Solution:
    def canPartition(self, nums):
        n = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]])
        return dp[n][s]
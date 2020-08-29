#coding:utf-8

'''
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
'''

'''
思路：
将问题转化为背包问题，给一个可装载重量为amount的背包和n个物品，每个物品的重量为coins[i],且每个物品的数量无限，问存在多少种方法，把背包装满。
'''

class Solution:
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount]
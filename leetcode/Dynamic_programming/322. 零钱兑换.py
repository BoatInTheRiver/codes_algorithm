#coding:utf-8

'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

'''


'''
1.dp[i] 最少用dp[i]枚硬币凑出i块钱
2.dp[i] = min(dp[i-coin[j]], dp[i])
3.dp[0] = 0
4.计算顺序：从小到大
'''
class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        # dp[0]、dp[1]、...dp[amount]
        dp = [float('INF')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(n):
                if i - coins[j] >= 0 and dp[i - coins[j]] != float('INF'):
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)

        if dp[amount] == float('INF'):
            return -1
        return dp[amount]
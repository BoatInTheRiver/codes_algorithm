#coding:utf-8
'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
'''

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if not prices:
            return 0
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[:i]))
        return dp[-1]
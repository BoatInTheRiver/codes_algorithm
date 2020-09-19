#coding:utf-8

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

'''

class Solution:
    def maxProfit(self, k, prices):
        if k > len(prices) // 2:
            return self.maxProfitNolimit(prices)
        else:
            cost = [float('inf')] * (k + 1)
            profit = [0] * (k + 1)
            for price in prices:
                for i in range(1, k + 1):
                    cost[i] = min(cost[i], price - profit[i - 1])
                    profit[i] = max(profit[i], price - cost[i])
            return profit[-1]

    def maxProfitNolimit(self, prices):
        '''
        因为买卖一次股票至少需要两天，当k大于prices数组长度的一半时，
        可理解为交易次数不限，则问题与122题相同。
        '''
        if not prices:
            return 0
        empty, hold = 0, -prices[0]
        for price in prices:
            empty, hold = max(empty, hold + price), max(hold, empty - price)
        return empty
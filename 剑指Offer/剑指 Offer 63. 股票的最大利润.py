#coding:utf-8
'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
'''

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        cost, profit = float('INF'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
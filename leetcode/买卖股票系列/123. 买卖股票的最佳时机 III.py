#coding:utf-8

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易(你必须在再次购买前出售掉之前的股票)。

'''
class Solution:
    def maxProfit(self, prices):
        cost1 = cost2 = float('inf')
        profit1 = profit2 = 0
        for price in prices:
            cost1 = min(cost1, price)
            profit1 = max(profit1, price - cost1)
            cost2 = min(cost2, price - profit1)
            profit2 = max(profit2, price - cost2)
        return profit2
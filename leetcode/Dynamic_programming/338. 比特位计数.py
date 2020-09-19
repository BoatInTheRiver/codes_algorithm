#coding:utf-8

'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例:
输入: 2
输出: [0,1,1]

'''

class Solution:
    def countBits(self, num):
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i // 2]
        return dp
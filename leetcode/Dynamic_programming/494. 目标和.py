#coding:utf-8

'''
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。


示例：
输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

'''

'''
添加正号的背包总和为n, 添加负号的背包综合为m，由题意知 n - m = target
而 n + m = sum(nums)，由两式解得n = (sum(nums) + target) / 2
转化为0-1背包问题，背包容量为n，有len(nums)个物品，如何用这些物品装满背包
'''
class Solution:
    def findTargetSumWays(self, nums, S):
        sum_nums = sum(nums)
        if sum_nums < S or (sum_nums + S) % 2 == 1:
            return 0
        p = (sum_nums + S) // 2
        dp = [0] * (n + 1)
        dp[0] = 1
        for num in nums:
            for i in range(p, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]
#coding:utf-8

'''
在计算机界中，我们总是追求用有限的资源获取最大的收益。
现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

'''

'''
问题转化为0-1背包问题，背包容量为m个0和n个1
dp[i][j]:背包容量为i个0和j个1时，满足条件的字符串的最大数量
'''
class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n + 1) for _ in  range(m + 1)]
        for s in strs:
            count0 = s.count('0')
            count1 = s.count('1')
            # 0-1背包问题将二维数组转化为一维数组时采用倒序
            # 完全背包则为正序
            for i in range(m, count0 - 1, -1):
                for j in range(n, count1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - count0][j - count1] + 1)
        return dp[m][n]
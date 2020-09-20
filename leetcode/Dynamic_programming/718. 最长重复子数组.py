#coding:utf-8

'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：
输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。

'''

class Solution:
    def findLength(self, A, B):
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res


    '''将dp数组转化为一维数组'''
    def findLength1(self, A, B):
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        res = 0
        for i in range(1, m + 1):
            for j in range(n, 0, -1):  #逆序
                if A[i - 1] == B[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                res = max(res, dp[j])
        return res

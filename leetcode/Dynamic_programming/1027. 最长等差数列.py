#coding:utf-8

'''
给定一个整数数组 A，返回 A 中最长等差子序列的长度。
回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。
并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。

'''

class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = [{} for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                d = A[i] - A[j]
                tmp = dp[j].get(d, 1) + 1
                dp[i][d] = tmp
            res = max(res, max(dp[i].values()))
        return res
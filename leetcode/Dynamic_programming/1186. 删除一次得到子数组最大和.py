#coding:utf-8

'''
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，
然后该子数组（剩下）的元素总和是所有子数组之中最大的。注意，删除一个元素后，子数组 不能为空。

'''

class Solution:
    def maximumSum(self, arr):
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        res = dp[0][0] = dp[0][1] = arr[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])
            res = max(res, max(dp[i][0], dp[i][1]))
        return res

#coding:utf-8

'''
我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。

示例:
输入:
A = [9,1,2,3,9]
K = 3
输出: 20
解释:
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.

'''

class Solution:
    def largestSumOfAverages(self, A, K):
        n = len(A)
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i - 1] + A[i - 1]
        dp = [[0] * (n + 1) for _ in range(K + 1)]
        for i in range(1, n + 1):
            dp[1][i] = ans[i] / i
        for k in range(2, K + 1):
            for i in range(k, n + 1):
                for j in range(k - 1, i):
                    dp[k][i] = max(dp[k][i], dp[k - 1][j] + (ans[i] - ans[j]) / (i - j))
        return dp[K][n]
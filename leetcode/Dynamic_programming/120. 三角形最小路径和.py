#coding:utf-8

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
'''

'''
第i行共有i + 1个数
1.确定状态：dp[i][j]表示从三角形顶部走到位置(i, j)的最小路径和
2.状态转移方程：dp[i][j] = dp[i-1][j-1] + triangle[i][j]
3.初始条件和边界情况：
当i = 0时，只有一个数，dp[0][0] = triangle[0][0]
当在第i行的最左侧时，只能从i - 1行的最左侧过来，此时dp[i][0] = dp[i-1][0] + triangle[i][0]
当在第i行的最右侧时，只能从i - 1行的最右侧过来，此时dp[i][i] = dp[i-1][i-1] + triangle[i][i]
4.返回结果是dp[n-1][0]、dp[n-1][1]...dp[n-1][n-1]的最小值
'''

class Solution:
    # def minimumTotal(self, triangle):
    #     n = len(triangle)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #     dp[0][0] = triangle[0][0]
    #     for i in range(1, n):
    #         dp[i][0] = dp[i - 1][0] + triangle[i][0]
    #         for j in range(1, i):
    #             dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
    #         dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
    #     return min(dp[n-1])

    def minimumTotal(self, triangle):
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
#coding:utf-8

'''
这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。
我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。
如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。

'''

class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        for i in range(1, min(f, target)):
            dp[1][i] = 1
        for i in range(2, d + 1):
            for j in range(i, min(target, i * f) + 1):
                for k in range(1, f + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % (10 ** 9 + 7)
        return dp[d][target]
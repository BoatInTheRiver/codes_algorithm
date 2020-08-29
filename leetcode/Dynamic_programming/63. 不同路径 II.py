#coding:utf-8

'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
'''

class Solution:
    def uniquePathWithObstacles(self, obstaclesGrid):
        m, n = len(obstaclesGrid), len(obstaclesGrid[0])
        if obstaclesGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstaclesGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, n):
            if obstaclesGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstaclesGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]
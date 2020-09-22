#coding:utf-8

'''
亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。
在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
游戏一直持续到所有石子都被拿走。
假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。

'''

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        memo = {}

        def dfs(i, M):
            if (i, M) in memo:
                return memo[(i, M)]
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            res = 0
            for x in range(1, 2 * M + 1):
                res = max(res, suffix_sum[i] - dfs(i + x, max(x, M)))
            memo[(i, M)] = res
            return res
        return dfs(0, 1)
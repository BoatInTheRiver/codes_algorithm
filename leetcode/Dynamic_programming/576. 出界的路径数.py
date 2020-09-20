#coding:utf-8

'''
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。
但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

'''

class Solution:
    def findPath(self, m, n, N, i, j):
        memo = {}
        def dfs(x, y, k):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if k == 0:
                return 0
            if (x, y, k) in memo:
                return memo[(x, y, k)]
            res = 0
            for di, dj in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                res += dfs(di, dj, k -1)
            memo[(x, y, k)] = res % (10 ** 9 + 7)
            return res % (10 ** 9 + 7)
        return dfs(i, j, N)
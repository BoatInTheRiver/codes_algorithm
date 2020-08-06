#coding:utf-8
'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例：
输入：m = 2, n = 3, k = 1
输出：3

'''

class Solution:
    def sumofdigit(self, x, y):
        res = 0
        while x:
            res += x % 10
            x //= 10
        while y:
            res += y % 10
            y //= 10
        return res
    def movingCount(self, m, n, k):
        def dfs(i,j):
            if i >= m or j >= n or self.sumofdigit(i, j) > k or (i, j) in marked:
                return
            marked.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)
        marked = set()
        dfs(0, 0)
        return len(marked)
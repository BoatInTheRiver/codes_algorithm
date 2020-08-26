#coding:utf-8

'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
'''

class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for _ in range(n)]
        res = []

        def backtrack(res, row):
            '''
            if 满足条件：
                res.append(路径)
                return
            '''
            if row == n:
                tmp = []
                for line in board:
                    t = ''.join(line)
                    tmp.append(t[:])
                res.append(tmp[:])
                return

            '''
            for 选择 in 选择列表：
                做选择
                backtrack(路径，选择列表)
                撤销选择
            '''
            for col in range(len(board[row])):
                # 排除不合法选择
                if not can_place(row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 进行下一行决策
                backtrack(res, row + 1)
                # 撤销选择
                board[row][col] = '.'

        def can_place(x, y):
            # 判断(x, y)坐标能否放皇后
            # 1.判断x行是否有皇后
            for i in range(0, y):
                if board[x][i] == 'Q':
                    return False
            # 2.判断y列是否有皇后
            for i in range(0, x):
                if board[i][y] == 'Q':
                    return False

            # 3.判断'/'方向是否有皇后
            for i in range(0, x):
                if x + y - i <= n - 1 and board[i][x+y-i] == 'Q':
                    return False
            # 4.判断'\'方向是否有皇后
            for index, i in enumerate(range(x-1, -1, -1)):
                s_y = y - (index + 1)
                if s_y >= 0:
                    if board[i][s_y] == 'Q':
                        return False
            return True

        backtrack(res, 0)
        return res
s = Solution()
print(s.solveNQueens(4))
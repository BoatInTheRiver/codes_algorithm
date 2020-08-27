#coding:utf-8

'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

'''

class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(s, left+1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s, left, right+1)
                s.pop()
        backtrack([], 0, 0)
        return res

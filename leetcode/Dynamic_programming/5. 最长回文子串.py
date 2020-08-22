#coding:utf-8

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
'''

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_len = 1
        start = 0
        for i in range(n):
            dp[i][i] = True
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
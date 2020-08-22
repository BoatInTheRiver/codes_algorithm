#coding:utf-8

'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
'''

class Solution:
    def countSubstring(self, s):
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = False
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
        return count
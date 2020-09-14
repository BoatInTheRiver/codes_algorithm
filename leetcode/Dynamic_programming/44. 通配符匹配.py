#coding:utf-8

'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *

'''

'''
1.dp[i][j]:字符串s的前i个字符和模式串p的前j个字符是否匹配
2.当s[i-1] == p[j-1] or p[j-1] == '?'，dp[i][j] = dp[i-1][j-1]
  当p[j-1] == '*'，'*'匹配空串，dp[i][j] = dp[i][j-1]
  当p[j-1] == '*'，'*'匹配字符串s的第i个字符，dp[i][j] = dp[i-1][j]
3.当s为空串，p为空串，dp[0][0] = True
  当s不为空串，p为空串，dp[0][j] = False
  上述两种情况合并为if j==0, dp[i][j] = True if i == 0 else False
  
类似题型：leetcode第10题:正则表达式匹配
'''

class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if j == 0:
                    dp[i][j] = True if i == 0 else False
                else:
                    if p[j - 1] != '*':
                        if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '?'):
                            dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = dp[i][j] or dp[i][j - 1]
                        if i > 0:
                            dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[m][n]
#coding:utf-8

'''

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
'''

'''
状态：dp[i][j] 为s的前i个与p的前j个是否匹配

状态转移：
    三种情况：
        1. 如果p[j]为字母： dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        2. p[j] == '.': dp[i][j] = dp[i-1][j-1]
        3. p[j] == '*':说明 p[j-1]可以匹配0次或者无数次
            1. 匹配0次：则p的最后两个字符不起作用 dp[i][j] = dp[i][j-2]
            2. 匹配多次：dp[i][j] = dp[i-1][j]
边界条件：
    dp[0][0] = True 空字符串相匹配
    dp[i][0] = False 非空串，空正则
    dp[0][j] 空串，非空正则，需要计算

'''

class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                # p为空串
                if j == 0:
                    dp[i][j] = True if i == 0 else False
                # p不为空
                else:
                    # p的第j个字符不为'*'
                    if p[j - 1] != '*':
                        if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                            dp[i][j] = dp[i - 1][j - 1]
                    # p的第j个字符为'*'
                    else:
                        # '*'匹配0次
                        if j > 1:
                            dp[i][j] = dp[i][j] or dp[i][j - 2]
                        # '*'匹配多次
                        if i > 0 and j > 1 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                            dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[m][n]
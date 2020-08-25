#coding:utf-8


'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
 
示例：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

'''

'''
dp[i][j]:从word1[:i] 转换成word2[:j]需要的最少操作数
当word[i-1] == word[j-1]:    dp[i][j] = dp[i-1][j-1]
当word[i-1] != word[j-1]:    dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
dp[i-1][j-1] + 1  为在word1中进行替换操作
dp[i-1][j] + 1  为word1中进行删除操作
dp[i][j-1] + 1  为在word1中进行插入操作
初始条件：dp[0][j] = j, dp[i][0] = i
'''

class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]
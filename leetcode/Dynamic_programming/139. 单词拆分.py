#coding:utf-8

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
'''

'''
1.确定状态：dp[i]为长度为i的s[:i]是否在字典中
2.状态转移方程：被j划分为两部分s[0:j]、s[j:i]
当dp[j] == True 且s[j:i]也在字典中，则dp[i]为True
3.初始条件和边界情况：dp[0] == True 

'''

class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]

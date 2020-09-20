#coding:utf-8

'''
把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以 s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目。 

'''

from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, p):
        n = len(p)
        if n == 0:
            return 0
        dp = defaultdict(int)
        dp[p[0]] = 1
        m = 1
        for i in range(1, n):
            if ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25:
                m += 1
            else:
                m = 1
            dp[p[i]] = max(dp[p[i]], m)
        return sum(dp.values())
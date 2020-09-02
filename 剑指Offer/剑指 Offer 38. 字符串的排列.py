#coding:utf-8
'''
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

'''

class Solution:
    def permutation(self, s):
        res = []
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            seen = set()
            for i in range(len(s)):
                if s[i] in seen:
                    continue
                seen.add(s[i])
                dfs(s[:i]+s[i + 1:], path + s[i])
        dfs(s, '')
        return res
#coding:utf-8

'''
给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。


示例：
输入：S = "ADOBECODEBANC", T = "ABC"
输出："BANC"

'''

from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    else:
                        need[c] += 1
                        i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return s[res[0]:res[1] + 1] if res[1] < len(s) else ''
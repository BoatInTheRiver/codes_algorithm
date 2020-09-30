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
        needs = defaultdict(int)
        for c in t:
            needs[c] += 1
        needs_cnt = len(t)
        min_len, res = float('inf'), ''
        left, right = 0, 0
        while right < len(s):
            if needs[s[right]] > 0:
                needs_cnt -= 1
            needs[s[right]] -= 1
            right += 1
            while needs_cnt == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if needs[s[left]] == 0:
                    needs_cnt += 1
                needs[s[left]] += 1
                left += 1
        return res

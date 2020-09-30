#coding:utf-8

'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        needs = Counter(s1)
        needsCnt = len(s1)
        left, right = 0, 0
        window = {}
        while right < len(s2):
            c = s2[right]
            if c not in needs:
                window.clear()
                right += 1
                left = right
            else:
                window[c] = window.get(c, 0) + 1
                if right - left + 1 == needsCnt:
                    if window == needs:
                        return True
                    window[s2[left]] -= 1
                    left += 1
                right += 1
        return False

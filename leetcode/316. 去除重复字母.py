#coding:utf-8

'''
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:
输入: "bcabc"
输出: "abc"

示例 2:
输入: "cbacdcbc"
输出: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s):
        seen = set()
        stack = []
        dic = {}
        for i, c in enumerate(s):
            dic[c] = i
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < dic[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
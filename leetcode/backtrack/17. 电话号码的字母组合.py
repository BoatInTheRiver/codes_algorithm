#coding:utf-8

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []

        def backtrack(combination, nextdigit):
            if not nextdigit:
                res.append(combination)
                return
            for letter in phone[nextdigit[0]]:
                backtrack(combination + letter, nextdigit[1:])
        backtrack('', digits)
        return res
    
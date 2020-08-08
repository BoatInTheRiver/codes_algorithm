#coding:utf-8
'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "

'''

class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for c in s:
            if c in dic:
                dic[c] = False
            else:
                dic[c] = True
        for c in s:
            if dic[c]:
                return c
        return ' '
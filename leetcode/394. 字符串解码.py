#coding:utf-8

'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入

'''

class Solution:
    def decodeString(self, s):
        res, mul = '', 0
        stack = []
        for c in s:
            if c == '[':
                stack.append([res, mul])
                res, mul = '', 0
            elif c == ']':
                last_res, cur_mul = stack.pop()
                res = last_res + cur_mul * res
            elif '0' <= c <= '9':
                mul = mul * 10 + int(c)
            else:
                res += c
        return res
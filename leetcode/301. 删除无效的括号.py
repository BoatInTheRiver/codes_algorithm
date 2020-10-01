#coding:utf-8

'''
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
说明: 输入可能包含了除 ( 和 ) 以外的字符。

'''

class Solution:
    def removeInvalidParentheses(self, s):
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i]+item[i+1:])
            level = next_level

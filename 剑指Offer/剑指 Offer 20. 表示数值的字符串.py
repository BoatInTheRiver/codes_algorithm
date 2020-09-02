#coding:utf-8
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。

'''

class Solution:
    def isNumber(self, s):
        s = s.strip()
        met_dot, met_e,met_digit = False, False, False
        for i, c in enumerate(s):
            if c in ('+', '-'):
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif c == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif c == 'e' or c =='E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif c.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

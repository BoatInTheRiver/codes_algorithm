#coding:utf-8
'''
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
'''

class Solution:
    def strToInt(self, str):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        flag = 0
        s = str.strip()
        if not s:
            return 0
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        if s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            flag = 0
            s = s[1:]
        for c in s:
            if c not in dic:
                break
            else:
                res = 10 * res
                res += dic[c]
        if flag == -1:
            return max(-res, INT_MIN)
        return min(res, INT_MAX)
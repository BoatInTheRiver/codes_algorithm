#coding:utf-8

'''
一个重复字符串是由两个相同的字符串首尾拼接而成，例如abcabc便是长度为6的一个重复字符串，而abcba则不存在重复字符串。
给定任意字符串，请帮小强找出其中的最长重复子串。
'''

s = input().strip()
n = len(s)
def getlen(s, n):
    for i in range(n // 2, 0, -1):
        count = 0
        for j in range(n - i):
            if s[j] != s[j + i]:
                if n - j <= 2 * i:
                    break
                count = 0
            else:
                count += 1
                if count == i:
                    return count * 2
    return 0
print(getlen(s, n))
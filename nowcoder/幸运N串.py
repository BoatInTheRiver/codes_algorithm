#coding:utf-8
'''
小A很喜欢字母N，他认为连续的N串是他的幸运串。有一天小A看到了一个全部由大写字母组成的字符串，
他被允许改变最多2个大写字母（也允许不改变或者只改变1个大写字母），使得字符串中所包含的最长的连续的N串的长度最长。你能帮助他吗？
'''

t = int(input())
for _ in range(t):
    s = input()
    li = []
    res = 0
    for c in s:
        li.append(c)
        if len(li) - li.count('N') >= 3:
            li.pop(0)
        res = max(res, len(li))
    print(res)
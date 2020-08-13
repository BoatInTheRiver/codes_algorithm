#coding:utf-8
'''
现有字符串text，找出text中重复出现最多的字符，然后将该字符移到text的最前端，生成一个新的字符串。
假设重复出现最多的字符只有一个。请充分考虑内存和性能效率。 举例： “abcaba”，转换后成为“aaabcb”。
'''
s = input().strip()
a = []
a += s
leng = 0
cnt = 0
idx = 0
for i, c in enumerate(a):
    cnt = a.count(c)
    if cnt > leng:
        leng = cnt
        idx = i
print(''.join(leng*[a[idx]] + list(s.replace(a[idx],''))))
#coding:utf-8
'''
小A刚学了二进制，他十分激动。为了确定他的确掌握了二进制，
你给他出了这样一道题目：给定N个非负整数，将这N个数字按照二进制下1的个数分类，二进制下1的个数相同的数字属于同一类。
求最后一共有几类数字？
'''


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    nums = list(map(bin, arr))
    dic = set()
    for num in nums:
        dic.add(num.count('1'))
    print(len(dic))
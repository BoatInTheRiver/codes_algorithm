#coding:utf-8
'''
小易有一个长度为n的数字数组a1, a2, …, an。
问你是否能用这n个数字构成一个环(首尾连接)，使得环中的每一个数字都小于它相邻的两个数字的和(每个数字都必须使用并且每个数字只能使用一次)。
'''
def check(h):
    n = len(h)
    h.sort()
    if h[n - 1] < h[n - 2] + h[0]:
        return True
    elif h[n - 1] < h[n - 2] + h[n - 3]:
        return True
    else:
        return False

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    res = check(h)
    if res:
        print('YES')
    else:
        print('NO')
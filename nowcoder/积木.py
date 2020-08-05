'''
小易有n堆积木，第i堆积木有hi块。小易还拥有一个容量无限的背包。
一开始小易站在第一堆积木旁边。每次小易可以选择进行下列三种操作中的一种：
1、从背包里掏出一块积木（如果有的话）放到当前这一堆里
2、从当前这一堆积木里掏出一块塞到背包里(如果当前积木堆不为空的话)
3、从当前这一堆走到下一堆。
一开始小易的背包里有m块积木。小易希望把这些个积木变成严格递增的（即h1<h2<h3<...<hn）
小易希望知道这是否有可能能完成。（所有操作结束后不需要保证背包里没有积木了，可以有积木堆为空）。

输入描述:
第一行数据组数T
对于每组数据，第一行数字n,m,接下来一行n个数字表示hi。
1<=n<=100000,0<=hi<=10**9,1<=T<=10,0<=m<=10**9。

输出描述:
对于每组数据输出一行，输出结果YES或NO
'''

def get(m, h):
    for i in range(len(h)):
        if h[i] > i:
            m += h[i] - i
        elif h[i] < i:
            if m + h[i] >= i:
                m -= i - h[i]
            else:
                return False
        else:
            continue
    return True
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    res = get(n, m, h)
    if not res:
        print('NO')
    else:
        print('YES')
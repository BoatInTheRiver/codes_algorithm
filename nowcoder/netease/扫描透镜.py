#coding:utf-8
'''
在N*M的草地上,提莫种了K个蘑菇,蘑菇爆炸的威力极大,兰博不想贸然去闯,而且蘑菇是隐形的.有一种叫做扫描透镜的物品可以扫描出隐形的蘑菇,
于是他回了一趟战争学院,买了2个扫描透镜,一个 扫描透镜可以扫描出(3*3)方格中所有的蘑菇,然后兰博就可以清理掉一些隐形的蘑菇.
问:兰博最多可以清理多少个蘑菇?
注意：每个方格被扫描一次只能清除掉一个蘑菇。
'''
def f(p, i, j):
    if p[i][j] > 0:
        return 1
    else:
        return 0

def maxNum(p, N, M):
    maxnum = 0
    x, y = 0, 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            tmp = f(p, i, j) + f(p, i + 1,j) + f(p,i + 2,j) + f(p, i, j + 1) + f(p, i + 1, j + 1) + f(p, i + 2, j + 1) +\
                f(p, i, j + 2) + f(p, i + 1, j + 2) + f(p, i + 2, j + 2)
            if tmp > maxnum:
                maxnum = tmp
                x, y = i, j
    ans = [maxnum, [x, y]]
    return ans

while True:
    try:
        N, M, K = list(map(int, input().split()))
        p = [[0] * (M + 3) for _ in range(N + 3)]
        for i in range(K):
            x, y = list(map(int, input().split()))
            p[x][y] += 1
        ans1 = maxNum(p, N, M)
        max1 = ans1[0]
        x, y = ans1[1]
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if p[i][j] > 0:
                    p[i][j] -= 1
        ans2 = maxNum(p, N, M)
        max2 = ans2[0]
        print(max1 + max2)
    except:
        break
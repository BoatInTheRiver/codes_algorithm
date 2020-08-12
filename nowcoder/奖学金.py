#coding:utf-8
'''
小v今年有n门课，每门都有考试，为了拿到奖学金，小v必须让自己的平均成绩至少为avg。每门课由平时成绩和考试成绩组成，满分为r。
现在他知道每门课的平时成绩为ai ,若想让这门课的考试成绩多拿一分的话，小v要花bi 的时间复习，不复习的话当然就是0分。
同时我们显然可以发现复习得再多也不会拿到超过满分的分数。为了拿到奖学金，小v至少要花多少时间复习。
'''

while True:
    try:
        n, r, avg = map(int, input().split())
        li= []
        for i in range(n):
            a, b = map(int, input().split())
            li.append([a,b])
        li = sorted(li, key=lambda x: x[1])
        current = sum([i[0] for i in li])
        target = n * avg - current
        times = 0
        if target > 0:
            i = 0
            while target > 0:
                while li[i][0] >= r:
                    i += 1
                times += li[i][1]
                li[i][0] += 1
                target -= 1
            print(times)
        else:
            print(0)
    except:
        break
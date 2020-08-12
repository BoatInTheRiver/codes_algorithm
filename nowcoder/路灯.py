#coding:utf-8
'''
一条长l的笔直的街道上有n个路灯，若这条街的起点为0，终点为l，第i个路灯坐标为ai ，每盏灯可以覆盖到的最远距离为d，
为了照明需求，所有灯的灯光必须覆盖整条街，但是为了省电，要使这个d最小，请找到这个最小的d。
'''

while True:
    try:
        n, l = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()
        res = max(arr[0], l - arr[-1])
        for i in range(n - 1):
            res = max(res, (arr[i+1]-arr[i]) / 2.0)
        print('%.2f' % res)
    except:
        break
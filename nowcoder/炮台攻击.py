#coding:utf-8
'''
黑默丁格有三个炮台,炮台能攻击到距离它R的敌人 (两点之间的距离为两点连续的距离,例如(3,0),(0,4)之间的距离是5),
如果一个炮台能攻击到敌人,那么就会对敌人造成1×的伤害.黑默丁格将三个炮台放在N*M方格中的点上,并且给出敌人的坐标. 问:那么敌人受到伤害会是多大?
'''

import math
def dis(x1,y1,x2,y2):
    res = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return res
while True:
    try:
        r,x1,y1,x2,y2,x3,y3,x0,y0 = map(int, input().split())
        dis1 = dis(x1,y1,x0,y0)
        dis2 = dis(x2,y2,x0,y0)
        dis3 = dis(x3,y3,x0,y0)
        print(dis1,dis2,dis3)
        tmp = 0
        li = [dis1,dis2,dis3]
        for i in range(len(li)):
            if li[i] <= r:
                tmp += 1
        print(str(tmp)+'x')
    except:
        break
#coding:utf-8

'''
房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。
在 k  时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。
灯的颜色要想 变成蓝色 就必须同时满足下面两个条件：
灯处于打开状态。
排在它之前（左侧）的所有灯也都处于打开状态。
请返回能够让 所有开着的 灯都 变成蓝色 的时刻 数目

'''

class Solution:
    def numTimesAllBlue(self, light):
        s = 0
        res = 0
        for i in range(len(light)):
            s += light[i]
            length = i + 1
            tmp = length * (length + 1) // 2
            if s == tmp:
                res += 1
        return res

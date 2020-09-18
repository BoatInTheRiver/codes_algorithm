#coding:utf-8

'''
在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
至少有一个空座位，且至少有一人坐在座位上。
亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
返回他到离他最近的人的最大距离。

'''

'''
解题思路:
1.计算首尾距离最近的人的最大距离。
2.计算两个人之间的空位距离，如果选择坐在两个人i，j之间，则最远距离为(j - i) // 2。
3.用一个变量res保存这三者的最大值并返回。

时间复杂度为O(n),n为seats的长度。
空间复杂度为O(1)，只用到一个res变量。
'''
def maxDistance(seats):
    '''
    :param seats: 是一个只包含0和1的列表，0表示座位空着，1表示这个座位有人坐着
    :return: 返回某人选择的座位离最近的人的距离的最大值
    '''
    count = 1
    res = 0
    i, j  = 0, len(seats) - 1
    for k, val in enumerate(seats):
        if val == 0:
            continue
        if count == 1:
            res = max(res, k - i)
            count = 0
        else:
            res = max(res, (k - i) // 2)
        i = k
    res = max(res, j - i)
    return res
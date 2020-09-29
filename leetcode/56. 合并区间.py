#coding:utf-8

'''
给出一个区间的集合，请合并所有重叠的区间。

示例:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

'''

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        res = []
        index = -1
        for i in range(len(intervals)):
            if index == -1 or res[index][1] < intervals[i][0]:
                res.append(intervals[i])
                index += 1
            else:
                res[index][1] = max(res[index][1], intervals[i][1])
        return res

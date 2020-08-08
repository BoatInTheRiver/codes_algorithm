#coding:utf-8
'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 
示例：
输入：target = 9
输出：[[2,3,4],[4,5]]

'''

class Solution:
    def findContinousSequence(self, target):
        i, j = 1, 1
        res = 0
        li = []
        while i <= target // 2:
            if res < target:
                res += j
                j += 1
            elif res > target:
                res -= i
                i += 1
            else:
                arr = list(range(i, j))
                li.append(arr)
                res -= i
                i += 1
        return li
#coding:utf-8

'''
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，
且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。

示例：
输入：[23,2,4,6,7], k = 6
输出：True
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。

'''

class Solution:
    def checkSubarraySum(self, nums, k):
        dic = {0: -1}
        s = 0
        for i, num in enumerate(nums):
            s += num
            if k != 0:
                s %= k
            if s in dic:
                if i - dic[s] > 1:
                    return True
            else:
                dic[s] = i
        return False
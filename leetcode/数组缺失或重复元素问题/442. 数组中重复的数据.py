#coding:utf-8

'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
'''

'''
思路：原地修改数组元素为负数作为标记
'''

class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            pos = abs(num) - 1
            if nums[pos] < 0:
                res.append(pos + 1)
            nums[pos] = -nums[pos]
        return res

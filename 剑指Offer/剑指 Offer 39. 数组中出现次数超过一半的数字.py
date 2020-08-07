#coding:utf-8
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 
示例:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

'''
class Solution:
    def majorityElement(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
            if dic[num] > (len(nums) // 2):
                return num
        return None
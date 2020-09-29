#coding:utf-8

'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
'''

'''
思路：尽可能到达最远位置(贪心)。
如果能到达某个位置，那一定能到达它之前的所有位置。

'''
class Solution:
    def canJump(self, nums):
        max_index = 0
        for i in range(len(nums)):
            if max_index >= i and max_index < i + nums[i]:
                max_index = i + nums[i]
            if max_index >= len(nums) - 1:
                return True
        return False
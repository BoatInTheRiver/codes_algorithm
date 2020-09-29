#coding:utf-8

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：
输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

'''

class Solution:
    def minSubArrayLen(self, s, nums):
        min_len = float('inf')
        left, right = 0, 0
        sub_sum = 0
        while right < len(nums):
            sub_sum += nums[right]
            right += 1
            while sub_sum >= s:
                min_len = min(min_len, right - left)
                sub_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0
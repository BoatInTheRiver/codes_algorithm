#coding:utf-8

'''
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例:
输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

'''

class Solution:
    def findNumberOfLis(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        len_count = [1] * n
        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        len_count[i] = len_count[j]
                    elif dp[j] + 1 == dp[i]:
                        len_count[i] += len_count[j]
            max_len = max(max_len, dp[i])
        res = 0
        for i in range(n - 1, -1, -1):
            if dp[i] == max_len:
               res += len_count[i]
        return res

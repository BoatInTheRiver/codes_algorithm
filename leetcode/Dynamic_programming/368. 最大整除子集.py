#coding:utf-8

'''
给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
如果有多个目标子集，返回其中任何一个均可。

'''

class Solution:
    def largestDivisibleSubsets(self, nums):
        n = len(nums)
        dp = [1] * n
        index_arr = [-1] * n
        nums.sort()
        mx = 0
        end = -1
        res = []
        for i in range(n):
            for j in range(i):
                if s[i] % s[j] == 0 and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
                    index_arr[i] = j
            if dp[i] > mx:
                mx = dp[i]
                end = i
        while end != -1:
            res.append(nums[end])
            end = index_arr[end]
        return res[::-1]
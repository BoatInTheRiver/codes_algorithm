#coding:utf-8


'''
给定一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例:
输入: nums = [3, 4, 2]
输出: 6
解释:
删除 4 来获得 4 个点数，因此 3 也被删除。
之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
'''

class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        # 获取数组中的最大值
        n = max(nums)
        # arr数组用于存放0-n每个数在nums数组中对应的个数
        arr = [0] * (n + 1)
        # dp[i]指数组nums中最大值为i能获得的最大点数
        dp = [0] * (n + 1)
        for num in nums:
            arr[num] += 1
        dp[1] = arr[1]
        for i in range(2, n + 1):
            # 选i,可获得点数i * arr[i],并删除i-1,再加上dp[i-2],即dp[i] = i * arr[i] + dp[i - 2]
            # 不选i,则dp = [i - 1]
            dp[i] = max(dp[i - 1], dp[i - 2] + i * arr[i])
        return dp[n]
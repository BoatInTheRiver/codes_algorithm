#coding:utf-8

'''
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

示例:
输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

'''

class Solution:
    def splitArray(self, nums, m):
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            count = 1
            tmp = 0
            for i in range(len(nums)):
                tmp += nums[i]
                if tmp > mid:
                    count += 1
                    tmp = nums[i]
            if count > m:
                low = mid + 1
            else:
                high = mid
        return low
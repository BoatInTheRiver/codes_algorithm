#coding:utf-8
'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
'''
import collections
class Solution:
    # def maxSlidingWindow(self, nums, k):
    #     if not nums:
    #         return []
    #     res = []
    #     for i in range(len(nums) - k + 1):
    #         res.append(max(nums[i:i + k]))
    #     return res

    # 使用双端队列构造单调队列解决滑动窗口最大值问题
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n * k == 0:
            return
        res = []
        queue = collections.deque()
        for i in range(n):
            if queue and i - queue[0] + 1 > k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            if i >= j - 1:
                res.append(nums[queue[0]])
        return res
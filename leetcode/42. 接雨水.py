#coding:utf-8

'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''

'''
left_max：左边的最大值，它是从左往右遍历找到的
right_max：右边的最大值，它是从右往左遍历找到的
left：从左往右处理的当前下标
right：从右往左处理的当前下标
定理一：在某个位置i处，它能存的水，取决于它左右两边的最大值中较小的一个。
定理二：当我们从左往右处理到left下标时，左边的最大值left_max对它而言是可信的，但right_max对它而言是不可信的。
定理三：当我们从右往左处理到right下标时，右边的最大值right_max对它而言是可信的，但left_max对它而言是不可信的。
对于位置left而言，它左边最大值一定是left_max，右边最大值“大于等于”right_max，这时候，如果left_max<right_max成立，
那么它就知道自己能存多少水了。无论右边将来会不会出现更大的right_max，都不影响这个结果。 
所以当left_max<right_max时，我们就希望去处理left下标，反之，我们希望去处理right下标。

摘录自：https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/327718/
'''
class Solution:
    def trap(self, height):
        max_left, max_right = 0, 0
        left, right = 0, len(height) - 1
        res = 0
        while left <= right:
            if max_left < max_right:
                res += max(0, max_left - height[left])
                max_left = max(max_left, height[left])
                left += 1
            else:
                res += max(0, max_right - height[right])
                max_right = max(max_right, height[right])
                right -= 1
        return res
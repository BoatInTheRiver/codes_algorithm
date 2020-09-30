#coding:utf-8

'''

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
'''

'''
将出现过的数字对应的数组下标上的元素值始终设为负数，那么数组中正数元素的下标可以表示缺失的元素。
'''

class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
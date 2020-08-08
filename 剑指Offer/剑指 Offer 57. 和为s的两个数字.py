#coding:utf-8
'''

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 ：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
'''

class Solution:
    # 哈希表
    # def twoSum(self, nums, target):
    #     dic = {}
    #     for i, num in enumerate(nums):
    #         if target - num in dic:
    #             return nums[dic[target - num]], nums[i]
    #         else:
    #             dic[num] = i

    # 双指针
    def twoSum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
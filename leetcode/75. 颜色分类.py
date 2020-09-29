#coding:utf-8

'''

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
'''

class Solution:
    def sortColors(self, nums):
        p1, p2, cur = 0, len(nums) - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p1] = nums[p1], nums[cur]
                cur += 1
                p1 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1
        return nums
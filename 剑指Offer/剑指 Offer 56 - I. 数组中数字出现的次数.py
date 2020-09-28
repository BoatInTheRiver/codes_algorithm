#coding:utf-8


'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 
示例 ：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

'''

class Solution:
    def singleNumbers(self, nums):
        s = 0
        for num in nums:
            s ^= num
        h = 1
        while s & h == 0:
            h <<= 1
        a, b = 0, 0
        for num in nums:
            if num & h == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
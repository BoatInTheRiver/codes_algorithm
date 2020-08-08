#coding:utf-8
'''

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。


示例:
输入: [7,5,6,4]
输出: 5
'''

class Solution:
    def reversePairs(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        result = self.reversePairs(left) + self.reversePairs(right)

        left.sort()
        right.sort()
        i = 0
        for j in range(len(right)):
            while i < len(left) and left[i] <= right[j]:
                i += 1
            result += len(left) - i
        return result
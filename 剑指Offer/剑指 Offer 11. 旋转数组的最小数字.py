#coding:utf-8
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例：
输入：[3,4,5,1,2]
输出：1
'''

class Solution:
    def minArray(self, numbers):
        i, j = 0, len(numbers) - 1
        while i < j:
            mid = (i + j) // 2
            if numbers[mid] > numbers[j]:
                i = mid + 1
            elif numbers[mid] < numbers[j]:
                j = mid
            else:
                j -= 1
        return numbers[i]

#coding:utf-8
'''

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。


示例:
输入: [7,5,6,4]
输出: 5
'''

class Solution:
    def reversePairs(self, nums):
        self.res = 0
        self.merge_sort(nums)
        return self.res

    def merge(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        l, r = 0, 0
        tmp = []
        while l < n1 and r < n2:
            if arr1[l] > arr2[r]:
               tmp.append(arr2[r])
               self.res += n1 - l
               r += 1
            else:
                tmp.append(arr1[l])
                l += 1
        return tmp + arr1[l:] + arr2[r:]

    def merge_sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        left = self.merge_sort(arr[:n//2])
        right = self.merge_sort(arr[n//2:])
        return self.merge(left, right)
    
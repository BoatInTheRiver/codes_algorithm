#coding:utf-8
'''
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
'''

class Solution:
    def getLeastNumbers(self, arr, k):
        if k >= len(arr):
            return arr
        l, r = 0, len(arr) - 1
        return self.quickselect(arr, l, r, k)

    def partition(self, arr, l, r):
        low, high = l, r
        base = arr[l]
        while low < high:
            while low < high and arr[high] >= base:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < base:
                low += 1
            arr[high] = arr[low]
        arr[low] = base
        return low
    def quickselect(self, arr, l, r, k):
        pos = self.partition(arr, l, r)
        if pos == k:
            return arr[:pos]
        elif pos > k:
            return self.quickselect(arr, l, pos - 1, k)
        else:
            return self.quickselect(arr, pos + 1, r, k)

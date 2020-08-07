#coding:utf-8
'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


示例:
输入: [10,2]
输出: "102"
'''

class Solution:
    def minNumber(self, nums):
        def fast_sort(li, left, right):
            if left >= right:
                return
            low = left
            high = right
            base = li[left]
            while low < high:
                while low < high and li[high] + base >= base + li[high]:
                    high -= 1
                li[low] = li[high]
                while low < high and li[low] + base <= base + li[low]:
                    low += 1
                li[high] = li[low]
            li[low] = base
            fast_sort(li, left, low - 1)
            fast_sort(li, low + 1, right)

        li = [str(num) for num in nums]
        fast_sort(li, 0, len(li) - 1)
        return ''.join(li)
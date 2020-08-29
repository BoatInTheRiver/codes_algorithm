#coding:utf-8

'''
算法思路:
每趟从待排序的数列中选出值最小的元素，顺序放在已排序序列的末尾，直到排序结束。

比较次数与数列的初始排序无关，因为总是要比较n*(n-1)/2次。最好最坏平均时间复杂度都是O(n^2)。是不稳定的排序算法。

'''
import random

def select_sort(nums):
    n = len(nums)
    if n == 0:
        return []
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if nums[min_index] > nums[i]:
                min_index = i
        nums[j], nums[min_index] = nums[min_index], nums[j]
    return nums

if __name__ == '__main__':
    nums = [random.randint(1,20) for i in range(10)]
    print(nums)
    select_sort(nums)
    print('排序后的数组为:{}'.format(nums))

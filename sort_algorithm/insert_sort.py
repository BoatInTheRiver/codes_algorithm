#coding:utf-8

'''
算法思想:
每一趟将一个待排序的元素按照其元素值的大小插入到有序队列的合适位置，直到全部插完。

当数列为正序时，每次插入都不用移动前面的元素，最好时间复杂度为O(n);当数列为反序时，每次插入都得让前面元素后移，最坏时间复杂为O(n^2)。
数列越接近正序，插入排序性能越好。因为不改变相等元素的位置，所以是稳定的排序算法。

算法优化：因为每次都是将一个元素插入到一个有序序列中，所以可以使用二分查找，减少元素比较次数。
'''
import random
def binary_search(nums, end, item):
    left, right = 0, end - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return left if left < end else -1

def insert_sort(nums):
    n = len(nums)
    if n == 0:
        return []
    res = nums
    for i in range(1, n):
        j = i - 1
        tmp = nums[i]
        insert_index = binary_search(res, i, nums[i])
        if insert_index != -1:
            while j >= insert_index:
                res[j + 1] = res[j]
                j -= 1
            res[j + 1] = tmp
    return res


if __name__ == '__main__':
    nums = [random.randint(1,20) for i in range(10)]
    print(nums)
    res = insert_sort(nums)
    print('排序后的数组为:{}'.format(res))


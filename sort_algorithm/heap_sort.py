#coding:utf-8

'''
算法思想：
堆排序是利用堆的性质进行的一种选择排序。
堆是一棵按顺序存储的完全二叉树。
其中每个节点的值都不大于其孩子节点的值，这样的堆叫小根堆。
其中每个节点的值都不小于其孩子节点的值，这样的堆叫大根堆。

堆排序的最好最坏平均时间复杂度都是O(nlogn)，空间复杂度为O(1)。是不稳定的排序算法。
TopK问题优先考虑堆排序和快速选择，https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

'''
import random

def heap_adjust(nums, parent, length):
    '''堆调整，调整为最大堆'''
    tmp = nums[parent]
    child = 2 * parent + 1
    while child < length:
        if child + 1 < length and nums[child] < nums[child + 1]:
            child += 1
        if tmp >= nums[child]:
            break

        nums[parent] = nums[child]

        parent = child
        child = 2 * parent + 1
    nums[parent] = tmp

def heap_sort(nums):
    n = len(nums)
    if n == 0:
        return []
    res = nums
    length = len(res)
    for i in range(length//2 - 1, -1, -1):
        heap_adjust(res, i, length)

    for j in range(length-1, 0, -1):
        res[j], res[0] = res[0], res[j]
        heap_adjust(res, 0, j)
        print('第{}趟排序: '.format(length-j), end='')
        print(res)
    return res

if __name__ == '__main__':
    nums = [random.randint(1,20) for i in range(10)]
    print(nums)
    res = heap_sort(nums)
    print('排序后的数组为:{}'.format(res))
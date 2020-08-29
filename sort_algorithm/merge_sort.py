#coding:utf-8

'''
算法思想:
采用分治法的思想，分即将问题分成小问题，然后递归求解，治是指将分阶段的各个答案合并在一起。

归并排序的形式是一棵二叉树，需要遍历的次数就是二叉树的深度。最好最坏平均时间复杂度都为O(nlogn),空间复杂度为O(n)。

归并排序是稳定算法。

归并排序、快速排序、堆排序比较：
若从空间复杂度来考虑，优先考虑堆排序，其次是快排，最后是归并。
若从稳定性来考虑，优先考虑归并排序，因为堆排序和快排都是不稳定的。
若从平均情况下的排序速度考虑，优先考虑快速排序。

'''
import random

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n // 2
    left_nums = merge_sort(nums[:mid])
    right_nums = merge_sort(nums[mid:])
    left_point, right_point = 0, 0
    res = []
    while left_point < len(left_nums) and right_point < len(right_nums):
        if left_nums[left_point] <= right_nums[right_point]:
            res.append(left_nums[left_point])
            left_point += 1
        else:
            res.append(right_nums[right_point])
            right_point += 1
    res += left_nums[left_point:]
    res += right_nums[right_point:]
    return res

if __name__ == '__main__':
    nums = [random.randint(1,20) for i in range(10)]
    print(nums)
    res = merge_sort(nums)
    print('排序后的数组为:{}'.format(res))
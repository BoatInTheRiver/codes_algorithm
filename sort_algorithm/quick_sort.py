#coding:utf-8

'''
算法思想:
通过一趟排序将要排序的数列分割成两部分，分割点左边都是小于它的数，右边都是大于它的数。
再按此方法对这两部分分别进行快速排序，整个排序过程可以递归进行，以此达到整个数列有序。

最坏情况:当数据有序时，以第一个关键字为基准分为两个子序列，前一个子序列为空，时间复杂度为O(n^2)。
最好情况:当数据随机分布，以第一个关键字为基准分为两个子序列，两个子序列的元素接近相等，时间复杂度为O(nlogn)。
平均时间复杂度为O(nlogn),空间复杂度为O(logn)。

在快速排序中，相等元素可能会因为分区而交换顺序，所以不是稳定算法。

算法优化:
快排基准的选择：1.固定基准 2.随机基准 3.三数取中
快速排序的优化：1.当分区序列长度比较小时，使用插入排序
              2.尾递归优化
              3.聚集元素
              4.多线程处理快排
参考文章：https://blog.csdn.net/qq_38289815/article/details/82718428

'''
import random

def quick_sort(nums, left, right):
    if left >= right:
        return
    low = left
    high = right
    base = nums[left]
    while low < high:
        while low < high and nums[high] >= base:
            high -= 1
        while low < high and nums[low] < base:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]
    nums[low] = base
    quick_sort(nums, left, low - 1)
    quick_sort(nums, low + 1, right)

if __name__ == '__main__':
    nums = [random.randint(1,20) for i in range(10)]
    print(nums)
    quick_sort(nums, 0, len(nums) - 1)
    print('排序后的数组为:{}'.format(nums))
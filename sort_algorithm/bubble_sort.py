#coding:utf-8

'''
算法思想(以升序为例):
重复访问要排序的数列，每次比较当前元素和它的下一个元素，如果当前元素的值比后面元素的值大则交换位置，
一趟比较完就会冒出一个最大值，再重头重复上述工作，直到没有元素交换，说明该数列排序完成。

冒泡排序是一种交换排序，最好情况为正序，数列比较n-1次，所以最好情况的时间复杂度为O(n);最坏情况为反序，需要比较n*(n+1)/2次，所以最坏
情况的时间复杂度为O(n^2);平均时间复杂度为O(n^2);当数据越接近正序，冒泡排序性能越好，因为冒泡排序不会改变相等元素的初始位置，所以是一种稳定的排序算法。

算法优化：增加一个计数器，当某一趟排序没有进行数据交换则说明数据已经有序，即可结束排序。
'''
import random

def bubble_sort(nums):
    n = len(nums)
    if n == 0:
        return []
    for j in range(n):
        # 新增计时器
        count = 0
        print('第{}趟排序: '.format(j + 1))
        for i in range(n - j - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count += 1
        print(nums)
        if count == 0:
            break
    return nums

if __name__ == '__main__':
    nums = [random.randint(1,20) for i in range(10)]
    print(nums)
    bubble_sort(nums)
    print('排序后的数组为:{}'.format(nums))



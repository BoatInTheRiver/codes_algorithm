#coding:utf-8

'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

'''

'''
解题思路：
1.使用哈希表判重，违反说明第二条。
2.将数组排序，重复的数相邻，违反说明第一条。
3.使用抽屉法(原地哈希)，当两个数发现要放在一个同一个地方就找到了重复的数，具体可见leetcode第41题，违反说明第一条。
4.使用快慢指针，灵感来源于力扣第142题，把数组看成链表，数组的下标看成指向元素的指针，对应的元素也为指针。将问题转化为找环形链表的入口。

'''

class Solution:
    def findDuplicate(self, nums):
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                return fast
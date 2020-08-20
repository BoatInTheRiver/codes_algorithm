# coding:utf-8

'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
示例:
输入: 1->1->2
输出: 1->2
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''递归'''
    def deleteDuplicates1(self, head):
        if not head or not head.next:
            return head
        node = self.deleteDuplicates1(head.next)
        if node.val == head.val:
            return node
        else:
            head.next = node
            return head

    '''迭代'''
    def deleteDuplicates2(self, head):
        if not head or not head.next:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
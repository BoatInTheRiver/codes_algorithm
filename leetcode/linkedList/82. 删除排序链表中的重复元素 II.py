# coding:utf-8

'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例:
输入: 1->2->3->3->4->4->5
输出: 1->2->5
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
        cur = head
        if head != head.next.val:
            head.next = self.deleteDuplicates1(head.next)
            return head
        else:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            return self.deleteDuplicates1(cur.next)
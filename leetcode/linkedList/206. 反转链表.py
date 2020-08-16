#coding:utf-8
'''
反转一个单链表。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return
        pre = None
        cur = head
        while cur:
            cur.next = pre
            pre = cur
            cur = cur.next
        return pre
#coding:utf-8
'''
反转一个单链表。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''迭代'''
    def reverseList(self, head):
        if not head:
            return
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    # '''递归'''
    # def reverseList(self,head):
    #     if not head or not head.next:
    #         return
    #     nextNode = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return nextNode
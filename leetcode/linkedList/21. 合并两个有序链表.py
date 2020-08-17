#coding:utf-8
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''递归'''
    # def mergeTwoLists(self, l1, l2):
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

    '''迭代'''
    def mergeTwoLists(self, l1, l2):
        dum = ListNode(0)
        tail = dum
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dum.next
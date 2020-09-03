#coding:utf-8
'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dum = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next


    # 递归思想
    def mergeTwoLists1(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists1(l1, l2.next)
            return l2
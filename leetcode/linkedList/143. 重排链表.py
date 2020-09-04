#coding:utf-8

'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        last = slow.next
        slow.next = None
        p = self.reverseList(last)
        q = head
        while p:
            tmp1 = q.next
            tmp2= p.next
            q.next = p
            p.next = tmp1
            q = tmp1
            p = tmp2
        return head

    def reverseList(self, head):
        if not head or not head.next:
            return head
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

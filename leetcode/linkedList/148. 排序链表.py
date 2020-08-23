#coding:utf-8

'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''快速排序'''
    def sortList1(self, head):
        if not head:
            return
        small, equal, big = None, None, None
        cur = head
        while cur:
            t = cur
            cur = cur.next
            if t.val < head.val:
                t.next = small
                small = t
            elif t.val > head.val:
                t.next = big
                big = t
            else:
                t.next = equal
                equal = t
        small = self.sortList(small)
        big = self.sortList(big)
        dummy = ListNode(0)
        p = dummy
        for node in [small, equal, big]:
            while node:
                p.next = node
                p = p.next
                node = node.next
        return dummy.next

    '''归并排序'''
    def sortList2(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid, slow.next = slow.next, None
        left = self.sortList2(head)
        right = self.sortList2(mid)
        dummy = ListNode(0)
        p = dummy
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return dummy.next
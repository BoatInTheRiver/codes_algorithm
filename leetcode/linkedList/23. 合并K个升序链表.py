#coding:utf-8
'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''

class Solution:
    '''利用归并的思想'''
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        return self.merge2Lists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))

    def merge2Lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge2Lists(l1, l2.next)
            return l2

    # '''暴力法'''
    # def mergeKlists(self, lists):
    #     l = []
    #     for node in lists:
    #         while node:
    #             l.append(node.val)
    #             node = node.next
    #     l.sort()
    #     dum = ListNode(0)
    #     tail = dum
    #     for i in l:
    #         tail.next = ListNode(i)
    #         tail = tail.next
    #     return dum.next
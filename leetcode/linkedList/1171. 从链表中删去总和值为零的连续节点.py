#coding:utf-8

'''
给你一个链表的头节点 head，请你编写代码，反复删去链表中由 总和 值为 0 的连续节点组成的序列，直到不存在这样的序列为止。
删除完毕后，请你返回最终结果链表的头节点。

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head):
        dummy = p = ListNode(0)
        dummy.next = head
        dic = {}
        s = 0
        while p:
            s += p.val
            dic[s] = p
            p = p.next
        s = 0
        p = dummy
        while p:
            s += p.val
            p.next = dic[s].next
            p = p.next
        return dummy.next
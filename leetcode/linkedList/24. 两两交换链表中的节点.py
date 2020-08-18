# coding:utf-8

'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
 
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    '''经典递归思想，自顶向下'''
    def swapPairs1(self, head):
        if not head or not head.next:
            return head
        node = head.next
        head.next = self.swapPairs1(node.next)
        node.next = head
        return node

    '''迭代版'''
    def swapPairs2(self, head):
        pre = ListNode(0)
        pre.next = head
        tmp = pre
        while tmp.next and tmp.next.next:
            start = tmp.next
            end = tmp.next.next
            tmp.next = end
            start.next = end.next
            end.next = start
            tmp = start
        return pre.next

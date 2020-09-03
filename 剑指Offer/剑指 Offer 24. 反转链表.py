#coding:utf-8
'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


    # 递归思想
    def reverseList1(self, head):
        if not head or not head.next:
            return head
        last = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return last
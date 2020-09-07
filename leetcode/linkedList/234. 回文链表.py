#coding:utf-8

'''
请判断一个链表是否为回文链表。

示例:
输入: 1->2
输出: false
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        last = self.reverseLinkedList(mid.next)
        while last:
            if head.val != last.val:
                return False
            else:
                head = head.next
                last = last.next
        return True

    def reverseLinkedList(self, head):
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
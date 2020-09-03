#coding:utf-8
'''
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head, k):
        def getlen(head):
            if not head:
                return
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        for i in range(getlen(head) - k):
            head = head.next
        return head


    # 双指针
    def getKthFromEnd1(self, head, k):
        if not head:
            return
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
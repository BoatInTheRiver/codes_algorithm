#coding:utf-8

'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        def helper(node):
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            return stack

        s1 = helper(l1)
        s2 = helper(l2)
        remaining = 0
        dummy = ListNode(0)
        while s1 or s2 or remaining != 0:
            tmp = remaining
            if s1:
                tmp += s1.pop()
            if s2:
                tmp += s2.pop()
            num = tmp % 10
            remaining = tmp // 10
            node = ListNode(num)
            node.next = dummy.next
            dummy.next = node
        return dummy.next
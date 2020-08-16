#coding:utf-8
'''
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1, num2 = 0, 0
        i, j = 0, 0
        while l1:
            num1 += l1.val * (10**i)
            l1 = l1.next
            i += 1
        while l2:
            num2 += l2.val * (10**j)
            l2 = l2.next
            j += 1
        li = []
        for k in str(num1 + num2):
            li.append(k)
        res = ListNode(int(li.pop()))
        pos = res
        for _ in range(len(li)):
            tmp = ListNode(int(li.pop()))
            pos.next = tmp
            pos = pos.next
        return res
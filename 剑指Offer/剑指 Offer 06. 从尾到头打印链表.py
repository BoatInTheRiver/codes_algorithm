#coding:utf-8
'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head):
        if not head:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

    # 递归思想
    def reversePrint1(self, head):
        if not head:
            return []
        return self.reversePrint1(head.next) + [head.val]
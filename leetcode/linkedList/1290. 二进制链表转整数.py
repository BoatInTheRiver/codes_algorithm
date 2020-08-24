#coding:utf-8

'''
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
请你返回该链表所表示数字的十进制值
'''

class Solution:
    def getDecimalValue(self, head):
        if not head:
            return
        cur = head
        res = 0
        while cur:
            res = res * 2 + cur.val
            cur = cur.next
        return res
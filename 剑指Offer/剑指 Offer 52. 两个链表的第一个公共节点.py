#coding:utf-8
'''
输入两个链表，找出它们的第一个公共节点。

'''

class Solution:
    def getIntersectionNode(self, headA, headB):
        node1, node2 = headA, headB
        while node1 != node2:
            if node1:
                node1 = node1.next
            else:
                node1 = headB
            if node2:
                node2 = node2.next
            else:
                node2 = headA
        return node1

#coding:utf-8

'''
对链表进行插入排序。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if not head:
            return
        dummy = ListNode(-1)
        dummy.next = head
        pre = head # pre指向排好序的链表的尾部
        cur = head.next
        while cur:
            if cur.val < pre.val:
                tmp = dummy
                while tmp.next.val < cur.val:
                    tmp = tmp.next
                # 循环跳出来的tmp和tmp.next之间cur的插入点
                pre.next = cur.next # 记录下一个新节点的位置
                cur.next = tmp.next  # 接下来两步是将cur插入到对应位置
                tmp.next = cur
                cur = pre.next  #将cur指向待插入的新节点
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next
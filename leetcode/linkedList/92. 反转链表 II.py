# coding:utf-8

'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''

class Solution:
    # 反转前n个节点
    def reverseN(self, head, n):
        if n == 1:
            return head
        last = self.reverseN(head.next, n - 1)
        successor = head.next.next
        head.next.next = head
        head.next = successor
        return last

    def reverseBetween(self, head, m, n):
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head
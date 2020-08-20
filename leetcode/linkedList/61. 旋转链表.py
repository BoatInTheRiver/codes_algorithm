# coding:utf-8

'''

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
'''

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        n = k % count
        fast, slow = head, head
        while n:
            fast = fast.next
            n -= 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
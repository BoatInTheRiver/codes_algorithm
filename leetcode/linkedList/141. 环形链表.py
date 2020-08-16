#coding:utf-8
'''
给定一个链表，判断链表中是否有环。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ''' 借助集合'''
    # def hasCycle(self, head):
    #     if not head:
    #         return
    #     dic = set()
    #     while head:
    #         if head in dic:
    #             return True
    #         else:
    #             dic.add(head)
    #             head = head.next
    #     return False

    '''快慢指针'''
    def hasCycle(self, head):
        if not head:
            return
        slow, fast = head, head
        while fast and slow:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast is slow:
                return True
        return False
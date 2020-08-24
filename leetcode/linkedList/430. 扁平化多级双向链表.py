#coding:utf-8

'''
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。
这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。
'''

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        if not head:
            return
        dummy = Node(0, None, head, None)
        self.dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next

    def dfs(self, prev, cur):
        if not cur:
            return prev
        cur.prev = prev
        prev.next = cur
        tmp = cur.next
        tail = self.dfs(cur, cur.child)
        cur.child = None
        return self.dfs(tail, tmp)

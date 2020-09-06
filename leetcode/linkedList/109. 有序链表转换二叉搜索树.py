#coding:utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 将链表先存进数组，再构造BST
    def sortedListToBST(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.buildBST(arr, 0, len(arr) - 1)

    def buildBST(self, arr, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        root = TreeNode(arr[mid])
        root.left = self.buildBST(arr, start, mid - 1)
        root.right = self.buildBST(arr, mid + 1, end)
        return root

    # 通过快慢指针找到链表中电，再构造BST
    def sortedListToBST1(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        pre.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

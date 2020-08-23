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
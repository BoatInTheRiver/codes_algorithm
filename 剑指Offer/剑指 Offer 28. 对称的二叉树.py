#coding:utf-8
'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recur(self, root, cur):
        if not root and not cur:
            return True
        if not root or not cur:
            return False
        return (root.val == cur.val) and self.recur(root.left, cur.left) and self.recur(root.right, cur.right)

    def mirrorTree(self, root):
        if not root:
            return
        node = TreeNode(root.val)
        node.left, node.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return node

    def isSymmetric(self, root):
        mir = self.mirrorTree(root)
        return self.recur(root, mir)
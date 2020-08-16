#coding:utf-8
'''
给定一个二叉树，检查它是否是镜像对称的。
'''

class Solution:
    def isSymmetric(self, root):
        return self.recur(root, root)
    def recur(self, node1, node2):
        if not node1 and node2:
            return True
        if not node1 or node2:
            return False
        if node1.val != node2.val:
            return False
        return self.recur(node1.left, node2.right) and self.recur(node1.right, node2.left)
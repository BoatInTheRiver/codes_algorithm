#coding:utf-8
'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
'''

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left and not root.right:
            return left + right + 1
        if root.left and root.right:
            return min(left, right) + 1
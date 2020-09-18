#coding:utf-8

'''
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
二叉搜索树保证具有唯一的值。
'''

class Solution:
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.left, L, R)
        if root.val > R:
            return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
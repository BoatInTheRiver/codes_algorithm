#coding:utf-8

'''
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root)
        self.pre = TreeNode(0)
        res = self.pre
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node.left = None
            self.pre.right = node
            self.pre = node
            dfs(node.right)
        dfs(root)
        return res.right
#coding:utf-8
'''
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
'''

class Solution:
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxSum = max(self.maxSum, left + right + node.val)
            return max(0, max(left, right) + node.val)
        dfs(root)
        return self.maxSum
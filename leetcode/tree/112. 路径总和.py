#coding:utf-8
'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。
'''

class Solution:
    def hasPathSum(self, root, sum):
        res = []
        path = []
        def dfs(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()

        dfs(root, sum)
        if len(res):
            return True
        else:
            return False
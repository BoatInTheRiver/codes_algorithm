#coding:utf-8

'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。
'''

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                    return
                path += '->'
                dfs(root.left, path)
                dfs(root.right, path)
        res = []
        dfs(root, '')
        return res
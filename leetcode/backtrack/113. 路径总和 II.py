#coding:utf-8

'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
'''

class Solution:
    def pathSum(self, root, sum):
        res = []
        def dfs(root, path, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(path[:])
                return
            if node.left:
                dfs(root.left, path, target)
                path.pop()
            if node.right:
                dfs(root.right, path, target)
                path.pop()
        dfs(root, [], sum)
        return res
    
#coding:utf-8

'''
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列。
'''

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(root, arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
            return arr
        return dfs(root1, []) == dfs(root2, [])
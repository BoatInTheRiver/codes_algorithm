#coding:utf-8

'''
给定一个 N 叉树，返回其节点值的后序遍历。

'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    '''递归'''
    def postorder(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            res.append(root.val)
        dfs(root)
        return res

    '''迭代'''
    def postorder1(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for child in node.children:
                    stack.append(child)
        return res[::-1]
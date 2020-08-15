#coding:utf-8
'''
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
'''

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        def bfs(root):
            queue = [root]
            while queue:
                tmp = []
                nxt = []
                for node in queue:
                    tmp.append(node.val)
                    for child in node.children:
                        nxt.append(child)
                res.append(tmp)
                queue = nxt
        bfs(root)
        return res

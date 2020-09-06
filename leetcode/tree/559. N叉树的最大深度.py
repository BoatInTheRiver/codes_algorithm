#coding:utf-8

'''
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        res = 0
        for child in root.children:
            res = max(res, self.maxDepth(child))
        return res + 1
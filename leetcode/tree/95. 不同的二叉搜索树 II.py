#coding:utf-8
'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        def build_tree(start, end):
            if start > end:
                return [None]
            tmp = []
            for i in range(start, end + 1):
                left_trees = build_tree(start, i - 1)
                right_trees = build_tree(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        tmp.append(cur_tree)
            return tmp
        res = build_tree(1, n)
        return res
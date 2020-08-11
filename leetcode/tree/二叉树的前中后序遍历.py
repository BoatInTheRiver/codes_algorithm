#coding:utf-8
'''
leetcode 题目144/94/145
给定一个二叉树，返回它的先/中/后序遍历。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归版本
class Solution:
    #先序
    # def preorderTraversal(self, root):
    #     res = []
    #     def recur(root):
    #         if not root:
    #             return
    #         res.append(root.val)
    #         recur(root.left)
    #         recur(root.right)
    #
    #     recur(root)
    #     return res
    #中序
    # def inorderTraversal(self, root):
    #     res = []
    #     def recur(root):
    #         if not root:
    #             return
    #         recur(root.left)
    #         res.append(root.val)
    #         recur(root.right)
    #
    #     recur(root)
    #     return res
    #后序
    # def postorderTraversal(self, root):
    #     res = []
    #
    #     def recur(root):
    #         if not root:
    #             return
    #         recur(root.left)
    #         recur(root.right)
    #         res.append(root.val)
    #
    #     recur(root)
    #     return res

    # 借助栈来完成遍历
    def preorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res

    def inorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def postorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
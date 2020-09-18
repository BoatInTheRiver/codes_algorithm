#coding:utf-8
'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
'''

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        res = 0
        stack = [(root, str(root.val))]
        while stack:
            node, s = stack.pop()
            if node.left:
                stack.append((node.left, s + str(node.left.val)))
            if node.right:
                stack.append((node.right, s + str(node.right.val)))
            if not node.left and not node.right:
                res += int(s)
        return res

    def sumNumbers1(self, root):
        def dfs(root, n):
            if not root:
                return 0
            n = n * 10 + root.val
            if not root.left and not root.right:
                return n
            return dfs(root.left, n) + dfs(root.right, n)
        return dfs(root, 0)
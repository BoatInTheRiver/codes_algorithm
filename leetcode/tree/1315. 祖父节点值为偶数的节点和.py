#coding:utf-8

'''
给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 0 。

'''

class Solution:
    def sumEvenGrandparent(self, root):
        queue = collections.deque()
        res = 0
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        res += node.left.left.val
                    if node.left.right:
                        res += node.left.right.val
                if node.right:
                    if node.right.left:
                        res += node.right.left.val
                    if node.right.right:
                        res += node.right.right.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
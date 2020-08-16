#coding:utf-8
'''
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
'''

class Solution:
    '''递归'''
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    ''' 广度优先BFS'''
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     queue = [(1, root)]
    #     depth = 0
    #     while queue:
    #         depth, node = queue.pop(0)
    #         if node.left:
    #             queue.append((depth + 1, node.left))
    #         if node.right:
    #             queue.append((depth + 1, node.right))
    #     return depth

    ''' 深度优先DFS'''
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_depth, node = stack.pop()
            depth = max(depth, cur_depth)
            if node.left:
                stack.append((cur_depth + 1, node.left))
            if node.right:
                stack.append((cur_depth + 1, node.right))
        return depth
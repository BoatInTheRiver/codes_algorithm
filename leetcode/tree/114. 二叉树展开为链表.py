#coding:utf-8
'''
给定一个二叉树，原地将它展开为一个单链表。
'''
class Solution:
    def flatten(self, root):
        '''
        Do not return anything, modify root in-place instead.
        '''
        if not root:
            return
        node = root.left
        if node:
            while node.right:
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right)
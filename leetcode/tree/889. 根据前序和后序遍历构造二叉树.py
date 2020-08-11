#coding:utf-8
'''
返回与给定的前序和后序遍历匹配的任何二叉树。
pre 和 post 遍历中的值是不同的正整数。

'''

# 先序和中序，中序和后序都能唯一确定一棵二叉树
# 而先序和后序不能唯一确定一颗二叉树

class Solution:
    def buildTree(self, pre, post):
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        idx = post.index(pre[1])
        root.left = self.buildTree(pre[1:idx + 2], post[:idx + 1])
        root.right = self.buildTree(pre[idx + 2:], post[idx + 1:-1])
        return root
#coding:utf-8

'''
给出一个完全二叉树，求出该树的节点个数。

完全二叉树的定义如下：
在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2h 个节点。

'''

class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        # 左子树的深度等于右子树的深度，说明左子树填满，右子树可能没填满，也可能填满
        if left == right:
            # return (2**left) + self.countNodes(root.right) 用左移代替2**left
            return (1 << left) + self.countNodes(root.right)
        else:
            # 左子树深度不等于右子树深度，说明右子树填满
            # return (2**right) + self.countNodes(root.left)
            return (1 << right) + self.countNodes(root.left)
    '''利用完全二叉树的性质，计算树的深度'''
    def depth(self, root):
        if not root:
            return 0
        count = 0
        while root:
            count += 1
            root = root.left
        return count
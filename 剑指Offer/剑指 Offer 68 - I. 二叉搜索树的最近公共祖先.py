#coding:utf-8
'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

'''
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                break
        return root

    # 递归
    def lowestCommonAncestor1(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor1(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor1(root.right, p, q)
        return root
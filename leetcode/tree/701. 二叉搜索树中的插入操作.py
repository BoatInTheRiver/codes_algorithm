#coding:utf-8

'''
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if cur.val > val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
        return root
    
    '''递归'''
    def insertIntoBST1(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST1(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST1(root.right, val)
        return root

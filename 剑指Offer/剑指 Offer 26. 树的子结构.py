#coding:utf-8
'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2

给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A, B):
        def check(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return check(A.left, B.left) and check(A.right, B.right)
        return bool(A and B) and (check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
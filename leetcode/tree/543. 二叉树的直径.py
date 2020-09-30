#coding:utf-8

'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

'''
class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        depth(root)
        return self.res
    
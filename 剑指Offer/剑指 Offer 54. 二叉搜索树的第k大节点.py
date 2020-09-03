#coding:utf-8
'''

给定一棵二叉搜索树，请找出其中第k大的节点。

示例:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
'''

class Solution:
    def kthLargest(self, root, k):
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            res.append(root.val)
            dfs(root.left)
        dfs(root)
        return res[k - 1]
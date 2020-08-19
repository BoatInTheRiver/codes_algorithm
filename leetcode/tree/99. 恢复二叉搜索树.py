# coding:utf-8

'''
二叉搜索树中的两个节点被错误地交换。
请在不改变其结构的情况下，恢复这棵树。
'''

class Solution:
    def recoverTree(self, root):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(root.left)
            res.append(node)
            dfs(root.right)
        dfs(root)
        x, y = None, None
        pre = res[0]
        for i in range(1, len(res)):
            if pre.val > res[i].val:
                y = res[i]
                if not x:
                    x = pre
            pre = res[i]
        if x and y:
            x.val, y.val = y.val, x.val
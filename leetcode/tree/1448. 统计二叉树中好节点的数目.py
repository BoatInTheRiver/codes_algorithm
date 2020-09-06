#coding:utf-8

'''
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
'''

class Solution:
    def goodNodes(self, root):
        self.res = 0
        curMax = float('-INF')
        def dfs(root, curMax):
            if not root:
                return
            if root.val >= curMax:
                self.res += 1
                curMax = root.val
            dfs(root.left, curMax)
            dfs(root.right, curMax)
        dfs(root, curMax)
        return self.res
#coding:utf-8

'''
在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。

'''

class Solution:
    def isCousins(self, root, x, y):
        depth = {}
        parent = {}
        def dfs(node, par=None):
            if not node:
                return
            depth[node.val] = 1 + depth[par.val] if par else 0
            parent[node.val] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]
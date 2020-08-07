#coding:utf-8
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''

class Solution
    def treeToDoublelyList(self, root):
        if not root:
            return
        self.pre = None

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
#coding:utf-8
'''

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''

#利用二叉搜索树的中序遍历是有序的(升序)来验证二叉搜索树
class Solution:
    def isValidBST(self, root):
        def inorder(root):
            WHITE, GRAY = 0, 1
            res = []
            stack = [(WHITE, root)]
            while stack:
                color, node = stack.pop()
                if not node:
                    continue
                if color == WHITE:
                    stack.append((WHITE, node.right))
                    stack.append((GRAY, node))
                    stack.append((WHITE, node.left))
                else:
                    res.append(node.val)
            return res

        arr = inorder(root)
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True
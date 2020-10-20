#coding:utf-8

'''
如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

    二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
    偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
    奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减

给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。

'''

class Solution:
    def isEvenOddTree(self, root):
        queue = [root]
        depth = 0
        while queue:
            temp = []
            for i in range(len(queue) - 1):
                if depth % 2 == 1:
                    if queue[i].val <= queue[i + 1].val:
                        return False
                else:
                    if queue[i].val >= queue[i + 1].val:
                        return False

            for node in queue:
                if node.val % 2 == depth % 2:
                    return False
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            depth += 1
            queue = temp
        return True
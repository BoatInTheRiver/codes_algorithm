#coding:utf-8

'''
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

'''

class Solution:
    def pathSum(self, root, sum):
        def dfs(root, sumlist, sum):
            if not root:
                return 0
            sumlist1 = [num + root.val for num in sumlist]
            sumlist1.append(root.val)
            count = 0
            for num in sumlist1:
                if num == sum:
                    count += 1
            return count + dfs(root.left, sumlist1, sum) + dfs(root.right, sumlist1, sum)
        return dfs(root, [], sum)
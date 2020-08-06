#coding:utf-8
'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
 
例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

'''

from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queque.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
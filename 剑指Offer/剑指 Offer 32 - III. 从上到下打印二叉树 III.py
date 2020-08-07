#coding:utf-8
'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，
第三行再按照从左到右的顺序打印，其他行以此类推。

 
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
  [20,9],
  [15,7]
]

'''

class Solution:
    def leverOrder(self, root):
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            tmp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2 == 1:
                    tmp.appendleft(node.val)
                else:
                    tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(tmp))
        return res



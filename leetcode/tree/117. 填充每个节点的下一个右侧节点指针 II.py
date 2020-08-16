#coding:utf-8
'''
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

'''

class Solution:
    def connect(self, root):
        if not root:
            return
        cur_level = [root]
        while cur_level:
            res = []
            next_level = []
            for node in cur_level:
                res.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(res) == 1:
                res[0].next = None
            else:
                for i in range(len(res) - 1):
                    res[i].next = res[i + 1]
                res[-1].next = None
            cur_level = next_level
        return root
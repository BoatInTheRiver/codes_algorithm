#coding:utf-8

'''
给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。
同时给定列表 G，该列表是上述链表中整型值的一个子集。
返回列表 G 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 G 中）构成的集合。
'''

class Solution:
    def numComponents(self, head, G):
        st = set(G)
        cur = head
        res = 0
        flag = False
        while cur:
            if cur.val in st:
                if not flag:
                    res += 1
                    flag = True
            else:
                flag = False
            cur = cur.next
        return res
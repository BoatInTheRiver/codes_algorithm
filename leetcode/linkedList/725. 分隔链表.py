#coding:utf-8

'''
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
返回一个符合上述规则的链表的列表。

举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
'''

class Solution:
    def splitListToParts(self, root, k):
        total_len = 0
        p = root
        while p:
            p = p.next
            total_len += 1
        sub_len = total_len // k
        remaining = total_len % k
        res = []
        cur = root
        for i in range(k):
            rea.append(cur)
            size = sub_len + (1 if remaining > 0 else 0)
            if cur:
                count = 1
                while count < size:
                    cur = cur.next
                    count += 1
                remaining -= 1
                tmp = cur.next
                cur.next = None
                cur = tmp
        return res
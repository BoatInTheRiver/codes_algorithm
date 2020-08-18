
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printLinkedList(self, listNode):
        if not listNode:
            return []
        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next
        return res

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(5)
    node1.next = node3
    node3.next = node2
    s = Solution()
    print(s.printLinkedList(node1))
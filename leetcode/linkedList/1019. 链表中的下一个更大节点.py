#coding:utf-8

'''
示例1：
输入：[2,1,5]
输出：[5,5,0]

示例2：
输入：[2,7,4,3,5]
输出：[7,0,5,5,0]

示例3：
输入：[1,7,5,1,9,2,5,1]
输出：[7,9,9,9,0,5,0,0]

'''

class Solution:
    '''借助两个栈来维护一个单调递增栈'''
    def nextLargerNodes(self, head):
        if not head:
            return
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        res = [0] * len(arr)
        stackA, stackB = [], []
        for i in range(len(arr)):
            while stackA and stackA[-1] < arr[i]:
                res[stackB[-1]] = arr[i]
                stackA.pop()
                stackB.pop()
            stackA.append(arr[i])
            stackB.append(i)
        return res
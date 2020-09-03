#coding:utf-8
'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

'''

class Solution:
    def constructArr(self, a):
        if not a:
            return []
        n = len(a)
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * a[i - 1]
        for j in range(n - 2, -1, -1):
            r[j] = r[j + 1] * a[j + 1]
        for i in range(n):
            l[i] = l[i] * r[i]
        return l
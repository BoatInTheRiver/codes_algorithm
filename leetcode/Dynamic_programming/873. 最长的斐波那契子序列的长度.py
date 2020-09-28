#coding:utf-8

'''
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是斐波那契式的：
    n >= 3
    对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。

'''

class Solution:
    def lenLongestFibSubseq(self, A):
        n = len(A)
        if n < 3:
            return 0
        dic = {}
        res = 0
        tmpA = set(A)
        for i in range(1, n):
            for j in range(i):
                d = A[i] - A[j]
                if d < A[j] and d in tmpA:
                    dic[(A[j], A[i])] = dic.get((d, A[j]), 2) + 1
                    res = max(res, dic[(A[j], A[i])])
        return res
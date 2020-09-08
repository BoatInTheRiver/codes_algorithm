#coding:utf-8

'''
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
'''

class Solution:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack1, stack2 = [], []
        for i in range(len(T)):
            while stack1 and stack1[-1] < T[i]:
                res[stack2[-1]] = i - stack2[-1]
                stack1.pop()
                stack2.pop()
            stack1.append(T[i])
            stack2.append(i)
        return res
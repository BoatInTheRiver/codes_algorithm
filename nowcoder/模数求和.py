#coding:utf-8
'''
现给定n个整数，并定义一个非负整数m，且令f(m) = (m%a1)+(m%a2)+...+(m%an)。
此处的X % Y的结果为X除以Y的余数。
现请你找出一个m，求出f(m)的最大值。
'''

# 假设m % x = x - 1 (x-1为能取到的最大余数，也就是说m+1是x的倍数)
# 如果m+1是所有数的倍数，则f(m)可以取到最大值，即m+1是所有数的最小公倍数
# f(m) = (a1 - 1) + (a2 - 1) + ... + (an - 1) = sum(a) - n

n = int(input())
a = list(map(int, input().split()))
print(sum(a) - n)
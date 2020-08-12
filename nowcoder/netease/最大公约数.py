#coding:utf-8
'''
辗转相除法求最大公约数
'''


# 最大公约数
def gcd(a, b):
    k = 1
    while k:
        k = a % b
        a = b
        b = k
    return a

# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

# print(lcm(7, 5))
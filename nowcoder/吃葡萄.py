'''
问题描述:
有3种葡萄，数量分别是a,b,c。 第一个人只吃1,2种葡萄，第二个人只吃2,3种葡萄，
第三个人只吃1,3种葡萄。问怎么安排让3人吃完所有的葡萄，
而且让吃的比较多的那个人吃的葡萄尽可能的少。
'''

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    f = [a, b, c]
    max_f = max(f)
    sum_f = sum(f)
    if sum_f - max_f >= max_f // 2:
        print((sum_f + 2) // 3)
    else:
        print((max_f + 1) // 2)
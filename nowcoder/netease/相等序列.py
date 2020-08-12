#coding:utf-8
'''
题目给定a1,a2...an，这样一个长度为n的序列，现在你可以给其中一些元素加上一个值x（只能加一次），
然后可以给另外一些值减上一个值x（只能减一次），剩下的元素不能再进行操作。问最后有没有可能找到一个值x使所有元素的值相等。
'''
k = int(input())
for _ in range(k):
    n = int(input())
    arr = list(map(int, input().split()))
    nums = list(set(arr))
    nums.sort()
    if len(nums) > 3:
        print('NO')
    elif len(nums) < 3:
        print('YES')
    else:
        if nums[0] + nums[2] == 2 * nums[1]:
            print('YES')
        else:
            print('NO')
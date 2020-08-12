#coding:utf-8
'''
有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，
使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
'''

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        k, d = map(int, input().split())
        arr_pos = [[1] * n for _ in range(k + 1)]
        arr_neg = [[1] * n for _ in range(k + 1)]
        for i in range(n):
            arr_pos[1][i] = a[i]
            arr_neg[1][i] = a[i]
        for i in range(2, k + 1):
            for j in range(i + 1, n):
                if a[j] > 0:
                    arr_pos = max(arr_pos[i - 1][max(j - d, 0):j]) * a[j]
                    arr_neg = min(arr_neg[i - 1][max(j - d, 0):j]) * a[j]
                else:
                    arr_pos = min(arr_neg[i - 1][max(j - d, 0):j]) * a[j]
                    arr_neg = max(arr_pos[i - 1][max(j - d, 0):j]) * a[j]
        print(max(arr_pos[k]))
    except:
        break
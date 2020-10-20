n = int(input())
arr = []
res = []
for _ in range(n):
    x, y = map(int,input().split())
    arr.append((x, y))
arr.sort(key=lambda x:x[0])
print(arr)
arr = [(1, 2), (4, 6), (5, 3), (7, 5), (9, 0)]
res.append(arr[-1])

max_y = arr[-1][1]

for i in range(len(arr) - 2, -1, -1):
    if arr[i][1] >= max_y:
        res.append(arr[i])
        max_y = arr[i][1]
for i in range(len(res)-1,-1,-1):
    print(res[i][0], res[i][1])
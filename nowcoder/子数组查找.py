def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        m = int(input())
        nums = list(map(int, input().split()))
        res = []
        for num in nums:
            if num in arr:
                i = arr.index(num)
                res.append(i)
        if len(res) <= 1:
            print(0)
        print(res[-1] - res[0] + 1)
main()
import math
def minCost(x, a, b):
    res = 0
    price = min(3 * a, b)
    remain = x % 1500
    base = price * (x // 1500)
    c1 = math.ceil(remain / 500) * a
    res = base + min(c1, b)
    return res

def main():
    t = int(input())
    for _ in range(t):
        x, a, b = map(int, input().split())
        print(minCost(x, a, b))

if __name__ == '__main__':
    main()
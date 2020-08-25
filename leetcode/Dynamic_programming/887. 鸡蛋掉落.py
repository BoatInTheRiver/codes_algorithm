#coding:utf-8

'''
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
'''

class Solution:
    def superEggDrop(self, K, N):
        memo = {}
        def dp(k, n):
            '''k个鸡蛋，n个楼层'''
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('INF')
            low, high = 1, n
            while low <= high:
                mid = (low + high) // 2
                broken = dp(k - 1, mid - 1) #蛋碎，鸡蛋个数-1，楼层区间缩小到[1, mid - 1]
                not_broken = dp(k, n - mid) #蛋没碎，鸡蛋个数不变，楼层区间缩小到[mid + 1, n]
                # dp(k, n) = min(res, max(dp(k-1, mid-1), dp(k, n-mid)) + 1)
                if broken > not_broken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, not_broken + 1)
            memo[(k,n)] = res
            return res
        return dp(K, N)
#coding:utf-8

'''
爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。
当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

'''

'''
dp[x]:为手上牌面为x，能获胜的概率(获胜是指最终牌面小于等于N)
dp[x] = (dp[x + 1], dp[x + 2],...,dp[x + W]) / W
参考题解：https://leetcode-cn.com/problems/new-21-game/solution/huan-you-bi-zhe-geng-jian-dan-de-ti-jie-ma-tian-ge/

'''

class Solution:
    def new21Game(self, N, K, W):
        dp = [1 if i <= N else 0 for i in range(K + W)]
        s = sum(dp[K:K + W])
        for i in range(K - 1, -1, -1):
            dp[i] = s / W
            s = s - dp[i + W] + dp[i]
        return dp[0]
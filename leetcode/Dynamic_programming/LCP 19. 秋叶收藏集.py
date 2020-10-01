#coding:utf-8

'''
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y，
其中字符 r 表示一片红叶，字符 y 表示一片黄叶。出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。
每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。
请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例：
输入：leaves = "rrryyyrryyyrr"
输出：2
解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

'''

'''
解题思路：
最终状态为ryr所需要的最少操作次数，以y开头的状态不符合题意，以r开头的状态则有r、ry、ryr。
以每一片树叶结尾的收藏集都可以有这三种状态。
若当前树叶为r：
    r状态：无需操作
    ry状态：min(上一个r状态, 上一个ry状态) + 1(把当前树叶变为y)
    ryr状态：min(上一个ry状态, 上一个ryr状态)
若当前树叶为y：
    r状态：上一r状态 + 1(把当前树叶变为r)
    ry状态：min(上一个r状态, 上一个ry状态)
    ryr状态：min(上一个ry状态, 上一个ryr状态) + 1(把当前树叶变为r)

该类多状态问题，先画出状态转移图，根据状态转移图来写代码就轻松多了。
相似题目：股票买卖系列几个题都可以用相同思路解决。
'''

class Solution:
    def minimumOperations(self, leaves):
        r, ry, ryr = 1 if leaves[0] == 'y' else 0, float('inf'), float('inf')
        for i in range(1, len(leaves)):
            if leaves[i] == 'r':
                r, ry, ryr = r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr) + 1
        return ryr
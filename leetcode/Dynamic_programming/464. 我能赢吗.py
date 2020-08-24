#coding:utf-8

'''
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。
如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

'''
'''
思路:
设置一个字典记录状态k下的胜负情况，True代表赢，False代表输。
情况1：如果给定的数字范围大于等于目标值，直接返回True；
情况2：如果给定的数字总和小于目标值，说明两个人都不可能赢，返回False；
情况3：如果给定的数字总和正好等于目标值，则给定的数只有为奇数才能赢；
情况4：如果现有选择的最大值比目标值大，则直接赢
情况5：如果在遍历中有某个数字的情况，直接返回结果
'''

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        s = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if maxChoosableInteger > desiredTotal:
            return True
        elif s < desiredTotal:
            return False
        elif s == desiredTotal:
            return maxChoosableInteger % 2 == 1

        seen = {}

        def canWin(choices, remainder):
            if choices[-1] >= remainder:
                return True
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]
            for i in range(len(choices)):
                # 对手回合
                if not canWin(choices[:i] + choices[i+1:], remainder - choices[i]):
                    seen[seen_key] = True
                    return True
            seen[seen_key] = False
            return False

        return canWin(list(range(1, maxChoosableInteger + 1)), desiredTotal)
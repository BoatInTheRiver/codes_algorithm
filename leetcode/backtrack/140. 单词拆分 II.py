#coding:utf-8

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。
返回所有这些可能的句子。

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]

'''

from typing import List

class Solution:

    # 部分用例超时
    # def wordBreak(self, s:str, wordDict:List[str]) -> List[str]:
#     #     n = len(s)
#     #     res = []
#     #
#     #     def backtrack(start, path):
#     #         if start == n:
#     #             res.append(path[1:])
#     #         for i in range(start, n):
#     #             if s[start:i + 1] in wordDict:
#     #                 backtrack(i + 1, path + " " + s[start:i + 1])
#     #     backtrack(0, '')
#     #     return res

    def wordBreak(self, s:str, wordDict:List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(start):
            if start == len(s):
                return [[]]
            res = []
            for i in range(start, len(s)):
                word = s[start:i + 1]
                if word in wordSet:
                    nextWordBreaks = backtrack(i + 1)
                    for nextWordBreak in nextWordBreaks:
                        res.append(nextWordBreak[:] + [word])
            return res
        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [' '.join(words[::-1]) for words in breakList]

#coding:utf-8
'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 
示例:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

'''

class Solution:
    # def lengthOfLongestSubString(self, s):
    #     滑动窗口
    #     if not s:
    #         return 0
    #     maxlen = 0
    #     window = []
    #     for c in s:
    #         if c in window:
    #             window = window[window.index(c) + 1:]
    #             window.append(c)
    #         else:
    #             window.append(c)
    #         maxlen = max(maxlen, len(window))
    #     return maxlen


    # dp[j]表示以s[j]为结尾的最长不重复子字符串
    def lengthOfLongestSubString(self, s):
        # 动态规划 + 哈希表
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            # 获取s[j]最近的相同字符的索引i
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            if tmp < j - i: # dp[j-1] < j - i
                tmp += 1
            else:
                tmp = j - i
            res = max(res, tmp) # dp[j] = max(dp[j-1], dp[j])
        return res
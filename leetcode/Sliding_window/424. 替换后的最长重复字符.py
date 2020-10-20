#coding:utf-8

'''
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
注意:
字符串长度 和 k 不会超过 104。

示例:
输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
'''

from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        n = len(s)
        left, right = 0, 0
        dic = defaultdict(int)
        history_max_num = 0
        while right < n:
            dic[s[right]] = dic.get(s[right], 0) + 1
            history_max_num = max(history_max_num, dic[s[right]])
            if right - left + 1 > history_max_num + k:
                dic[s[left]] -= 1
                left += 1
            right += 1
        return n - left

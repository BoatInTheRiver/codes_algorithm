#coding:utf-8

'''

如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。
'''

class Solution:
    def longestDiverseString(self, a, b, c):
        dic = {'a':min(a, 2 * (b + c + 1)), 'b':min(b, 2 * (a + c + 1)), 'c':min(c, 2 * (a + b + 1))}
        n = sum(dic.values())
        res = []
        for _ in range(n):
            candidates = set(['a', 'b', 'c'])
            if len(res) > 1 and res[-1] == res[-2]:
                candidates.remove(res[-1])
            tmp = max(candidates, key=lambda x:dic[x])
            res.append(tmp)
            dic[tmp] -= 1
        return ''.join(res)
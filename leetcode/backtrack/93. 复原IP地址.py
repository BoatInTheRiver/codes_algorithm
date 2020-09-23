#coding:utf-8

'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。


示例：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s) <= 12:
            return []
        res = []
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) == 4 and start < len(s):
                return
            for length in range(1, 4):
                if start + length - 1 >= len(s):
                    return
                if length == 1 and s[start] == '0':
                    return
                strs = s[start:start + length]
                if length == 3 and int(strs) > 255:
                    return
                path.append(strs)
                backtrack(start + length, path)
                path.pop()
        backtrack(0, [])
        return res
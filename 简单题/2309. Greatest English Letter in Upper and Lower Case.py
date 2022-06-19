class Solution:
    def greatestLetter(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = 0
        ss = ord('a') - ord('A')
        res = ''
        for i in range(ord('A'), ord('Z') + 1):
            if chr(i) in d and chr(i + ss) in d:
                res = chr(i)
        return res

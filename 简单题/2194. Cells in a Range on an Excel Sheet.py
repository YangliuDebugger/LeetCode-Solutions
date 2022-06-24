class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c = s[0]
        res = []
        while c <= s[3]:
            num = s[1]
            while num <= s[4]:
                res.append(c+num)
                num = chr(ord(num) + 1)
            c = chr(ord(c) + 1)
        return res
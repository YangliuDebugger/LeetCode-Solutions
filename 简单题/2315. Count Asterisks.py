class Solution:
    def countAsterisks(self, s: str) -> int:
        L = s.split('|')
        cnt = 0
        for idx, i in enumerate(L):
            if idx % 2 == 0:
                cnt += i.count('*')
        return cnt

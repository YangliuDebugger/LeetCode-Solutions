class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            d[i] = 0
        for i in s:
            d[i] += 1
        for i in t:
            d[i] -= 1
        return sum([abs(d[i]) for i in d])

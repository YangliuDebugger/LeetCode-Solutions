class Solution:
    def minSteps(self, s: str, t: str) -> int:
        R = "abcdefghijklmnopqrstuvwxyz"
        D1 = {}
        D2 = {}
        for i in R:
            D1[i] = 0
            D2[i] = 0

        for i in s:
            D1[i] += 1

        for i in t:
            D2[i] += 1

        diff = 0
        for i in R:
            diff += abs(D1[i] - D2[i])

        return diff // 2

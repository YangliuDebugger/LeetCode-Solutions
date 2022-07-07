# Almost same question as Stone Game II
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cursum = [0] * (len(stoneValue) + 1)
        for idx in range(len(stoneValue)):
            cursum[idx + 1] = cursum[idx] + stoneValue[idx]
        N = -10 ** 9 + 7

        @cache
        def dp(start):
            if start >= len(stoneValue):
                return 0
            else:
                t = N
                for x in range(1, 4):
                    t = max(t, cursum[-1] - cursum[start] - dp(start + x))
            return t

        alice = dp(0)
        if alice * 2 > cursum[-1]:
            return "Alice"
        elif alice * 2 == cursum[-1]:
            return "Tie"
        return "Bob"
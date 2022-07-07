class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        cursum = [0] * (len(piles) + 1)
        for idx in range(len(piles)):
            cursum[idx + 1] = cursum[idx] + piles[idx]

        @cache
        def OpTimal(start, M):
            if start >= len(piles):
                return 0
            if 2 * M >= len(piles) - start:
                return cursum[-1] - cursum[start]
            else:
                t = 0
                for x in range(1, 2 * M + 1):
                    t = max(t, cursum[-1] - cursum[start] - OpTimal(start + x, max(x, M)))

            return t

        return OpTimal(0, 1)
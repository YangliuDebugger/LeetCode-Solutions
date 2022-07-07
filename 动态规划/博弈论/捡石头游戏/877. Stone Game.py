class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(low, high): # dp record the difference between me and him
            if low == high: return piles[low]
            return max(piles[low] - dp(low+1, high), piles[high] - dp(low, high-1))
        return dp(0, len(piles)-1) > 0
from functools import cache


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # basically, calculate the least money for any given range
        @cache
        def dp(low, high):
            if low >= high:
                return 0
            best = 100000000
            for i in range(low, high + 1):
                best = min(best, i + max(dp(low, i - 1), dp(i + 1, high)))
            return best

        return dp(1, n)

solution = Solution()
print(solution.getMoneyAmount(200))
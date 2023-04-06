class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # # top down
        # @cache
        # def dp(n, k):
        #     if n == k:
        #         return sum(reward1[:k])
        #     elif k == 0:
        #         return sum(reward2[:n])
        #     else:
        #         return max(dp(n-1, k) + reward2[n-1], dp(n-1, k-1) + reward1[n-1])
        # return dp(len(reward1), k)

        # this is sorting problem, dp time complexityt is O(k * n)
        # to start, we have reward as sum(reward2), we want to flip the value from reward2 to reward1 for exact k times
        t = sum(reward2)
        y = sorted([i - j for i, j in zip(reward1, reward2)], key=lambda x: -x)
        return t + sum(y[:k])


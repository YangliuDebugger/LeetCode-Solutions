class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # dp的题目
        dp = [[0] * (high * 2+1) for  i in range(2)]
        dp[0][zero] = 1
        dp[1][one] = 1
        cnt = 0
        N = 10 ** 9 + 7
        for i in range(1, high+1):
            z = (dp[0][i] + dp[1][i]) % N

            dp[0][i+zero] += z
            dp[1][i+one] += z
            if low <= i <= high:
                cnt += z % N
        return cnt % N
class Solution:
    def countHousePlacements(self, n: int) -> int:
        # 经典dp
        N = 10 ** 9 + 7
        dp = [1] * 4 # 00, 01, 10, 11
        for i in range(2, n+1):
            dp =[x % N for x in [dp[0]+dp[1]+dp[2]+dp[3], dp[0]+dp[2], dp[0]+dp[1], dp[0]]]
        return sum(dp) % N
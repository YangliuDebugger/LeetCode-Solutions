class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # 数学题，递推
        dp = [0] * 1000
        dp[0] = 1
        N = 10 ** 9 + 7
        # print(f"day 1, {dp[:20]}")
        for day in range(2, n+1):
            dp_tmp = [0] * 1000
            for i in range(0, delay):
                dp_tmp[i+1] = dp[i]
            for i in range(delay-1, forget-1):
                dp_tmp[0] = dp_tmp[0] + dp[i]
                dp_tmp[i+1] = dp[i]
            for i in range(1000):
                dp_tmp[i] %= N
            # print(f"day {day}, {dp[:20]}")

            dp = dp_tmp
        return sum(dp) % N
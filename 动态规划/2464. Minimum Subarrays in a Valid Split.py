class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n + 1)]
        if nums[0] == 1:
            return -1
        dp[1] = 1
        dp[0] = 0

        for i in range(1, n):
            if nums[i] == 1:
                dp[i + 1] = -1
                continue

            if dp[i] == -1:
                dp[i + 1] = -1
            else:
                dp[i + 1] = dp[i] + 1

            for j in range(i):
                if dp[j] != -1 and (dp[j] + 1 < dp[i + 1] or dp[i + 1] == -1):
                    if math.gcd(nums[i], nums[j]) > 1:
                        dp[i + 1] = dp[j] + 1
        print(dp)
        return dp[n]
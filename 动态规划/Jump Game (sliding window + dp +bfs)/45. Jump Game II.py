class Solution:
    def jump(self, nums: List[int]) -> int:
        # 正向dp (bottom up)
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for idx, i in enumerate(nums):
            for j in range(1, i + 1):
                if idx + j >= len(nums):
                    break
                dp[idx + j] = min(dp[idx + j], dp[idx] + 1)
        return dp[-1]

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # dp的问题
        n = len(nums)

        if n == 2:
            return nums[0] == nums[1]

        dp = [0] * n
        if nums[0] == nums[1]:
            dp[1] = 1
        if nums[0] == nums[1] and nums[0] == nums[2]:
            dp[2] = 1
        if nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]:
            dp[2] = 1

        for i in range(3, n):
            if nums[i] == nums[i - 1] and dp[i - 2] == 1:
                dp[i] = 1
            if nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2] and dp[i - 3] == 1:
                dp[i] = 1
            if nums[i] == nums[i - 1] + 1 and nums[i - 1] == nums[i - 2] + 1 and dp[i - 3] == 1:
                dp[i] = 1
        # print(dp)
        if dp[n - 1] == 1:
            return True
        return False

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp problem with very large k, sliding window maximum
        from collections import deque
        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = deque([0])
        for i in range(1, len(nums)):
            if q[0] < i - k:
                q.popleft()
            dp[i] = nums[i] + dp[q[0]]
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
        return dp[-1]


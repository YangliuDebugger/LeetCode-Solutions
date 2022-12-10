class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        t = sum(nums)
        cur = 0
        z = nums[0]
        for i in nums:
            cur += i
            z = max(z, max(cur, t))
            t -= i
        return z
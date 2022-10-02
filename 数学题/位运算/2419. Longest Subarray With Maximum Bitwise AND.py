class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        x = max(nums)
        cnt = 0
        maxcnt = 1

        for i in nums:
            if i == x:
                cnt += 1
            else:
                maxcnt = max(cnt, maxcnt)
                cnt = 0
        maxcnt = max(cnt, maxcnt)
        return maxcnt
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # double pointer
        v = 0
        start = 0
        end = 0
        bestl = 1
        while end < len(nums):
            while end < len(nums) and v & nums[end] == 0:
                v |= nums[end]
                end += 1
            bestl = max(bestl, end - start)
            if end == len(nums):
                break
            # print(start, end)
            v -= nums[start]
            start += 1
            if start > end:
                end = start
                v = 0
        return bestl


